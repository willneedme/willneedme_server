
import yahoofinancials
import requests
import pandas as pd
from flask import Blueprint, jsonify, request
import yfinance as yf
import numpy as np
import sys
import pymysql
import os
import json
import math
import pymysql
from yahoo_fin import stock_info, news, options
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import and_, or_, func
from datetime import datetime
from models.adminUser import AdminUser
from models.tickers import Tickers
from models.ticker_charts import TickerCharts
from db.database import connection, session
from utils.nasdaq import Nasdaq
from utils.date import yearMonthDay
from middleware.auth import auth
from operator import itemgetter
from GoogleNews import GoogleNews


finance = Blueprint("finance", __name__)


@finance.route("/chartdata", methods=["GET"])
@auth
def chartData():
    cursor = connection().cursor(pymysql.cursors.DictCursor)
    cursor.execute("select symbol from tickers")
    rows = cursor.fetchall()
    chartList = []
    # Getting a chart Data
    for i in range(0, len(rows)):
        try:
            # data = Nasdaq.allSymbol()
            history = stock_info.get_data(
                'AAPL', start_date="20220101",  interval="1d").reset_index().to_dict("records")

            # print(f"symbol:::{len(history)}", file=sys.stderr)
            for data in history:
                temp = insert(TickerCharts).values(
                    symbol=rows[i]["symbol"],
                    close=0 if math.isnan(data["close"]) else data["close"],
                    high=0 if math.isnan(data["high"]) else data["high"],
                    open=0 if math.isnan(data["open"]) else data["open"],
                    low=0 if math.isnan(data["low"]) else data["low"],
                    volume=0 if math.isnan(data["volume"]) else data["volume"],
                    date=datetime.strptime(
                        str(data["index"]), '%Y-%m-%d %H:%M:%S'),
                    symbolDate=f"{rows[i]['symbol']}{data['index']}"
                ).on_duplicate_key_update(
                    close=0 if math.isnan(data["close"]) else data["close"],
                    high=0 if math.isnan(data["high"]) else data["high"],
                    open=0 if math.isnan(data["open"]) else data["open"],
                    low=0 if math.isnan(data["low"]) else data["low"],
                    volume=0 if math.isnan(data["volume"]) else data["volume"],
                )
                session.execute(temp)
            session.commit()
            chartList = []
        except (TypeError, ValueError, Exception) as e:
            print(f"error symbol ::{rows[i]['symbol']}{e}")
            continue
    return ('', 204)


@finance.route("/daychart", methods=["GET"])
@auth
def dayChart():
    return jsonify(None)
    cursor = connection().cursor(pymysql.cursors.DictCursor)
    cursor.execute("select symbol from tickers")
    rows = cursor.fetchall()
    for row in rows:
        try:
            oneDay = yf.Ticker(row["symbol"]).history(period="1d")
            print(f"count:::{row['symbol']}")
            reset = oneDay.reset_index()
            history = reset.to_dict("records")
            for data in history:
                temp = insert(TickerCharts).values(
                    symbol=row["symbol"],
                    close=data["Close"],
                    high=data["High"],
                    open=data["Open"],
                    low=data["Low"],
                    date=data["Date"],
                    volume=data["Volume"],
                    symbolDate=f"{row['symbol']}{data['Date']}"
                ).on_duplicate_key_update(
                    close=data["Close"],
                    high=data["High"],
                    open=data["Open"],
                    low=data["Low"],
                    volume=data["Volume"],)
                session.execute(temp)
        except (TypeError, ValueError) as e:
            continue
    session.commit()
    return ('', 204)


@finance.route("/search/<query>", methods=["GET"])
@auth
def search(query):
    try:
        tickers = session.query(
            Tickers.symbol,
            Tickers.name,
            Tickers.marketCap)\
            .filter(or_(Tickers.symbol.like("%{}%".format(query)), Tickers.name.like("%{}%".format(query))))

        tickers_result = [dict(row) for row in tickers]

        return jsonify(tickers_result)
    except Exception as e:
        print(e, file=sys.stderr)
        session.rollback()
        return jsonify(None)


@finance.route("/ticker/<symbol>", methods=["GET"])
@auth
def ticker(symbol):
    try:
        ticker = session.query(Tickers.industry, Tickers.sector, Tickers.netChange)\
            .filter(Tickers.symbol == symbol).first()
        company = stock_info.get_company_info(
            symbol).reset_index().to_dict("records")
        logoUrl = ""
        for value in company:
            if value["Breakdown"] == "website":
                logo = str(value["Value"]).split(".")
                logoUrl = "https://logo.clearbit.com/{}.{}".format(
                    logo[len(logo) - 2], logo[len(logo) - 1])
        info = stock_info.get_quote_data(symbol)
        obj = {
            "logoUrl": logoUrl,
            "industry": ticker["industry"] if ticker is not None else "",
            "sector": ticker["sector"] if ticker is not None else "",
            "netChange": ticker["netChange"] if ticker is not None else 0,
            "name": info["shortName"] if "shortName" in info and info["shortName"] is not None else "",
            "averageVolumeThreeMonth": info["averageDailyVolume3Month"] if "averageDailyVolume3Month" in info and info["averageDailyVolume3Month"] is not None else 0,
            "averageVolumeTenDay": info["averageDailyVolume10Day"] if "averageDailyVolume10Day" in info and info["averageDailyVolume10Day"] is not None else 0,
            "fiftyDayAverage": info["fiftyDayAverage"] if "fiftyDayAverage" in info and info["fiftyDayAverage"] is not None else 0,
            "fiftyTwoWeekHigh": info["fiftyTwoWeekHigh"] if "fiftyTwoWeekHigh" in info and info["fiftyTwoWeekHigh"] is not None else 0,
            "fiftyTwoWeekLow": info["fiftyTwoWeekLow"] if "fiftyTwoWeekLow" in info and info["fiftyTwoWeekLow"] is not None else 0,
            "marketCap": info["marketCap"] if "marketCap" in info and info["marketCap"] is not None else 0,
            "symbol": info["symbol"] if "symbol" in info and info["symbol"] is not None else 0,
            "trailingPE": info["trailingPE"] if "trailingPE" in info and info["trailingPE"] is not None else 0,
            "twoHundredDayAverage": info["twoHundredDayAverage"] if "twoHundredDayAverage" in info and info["twoHundredDayAverage"] is not None else 0
        }
        charts = stock_info.get_data(
            symbol, interval="1d", index_as_date=False).reset_index().to_dict("records")

        for row in charts:
            row["date"] = row["date"].isoformat()
        result = [row for row in charts if math.isnan(row['open']) is False]
        # sortedChart = sorted(charts, key=(lambda x: x['date']), reverse=True)
        obj["charts"] = result

        return jsonify(obj)
    except Exception as e:
        print(e, file=sys.stderr)
        session.rollback()
        # remove tickers
        return jsonify(None)


@finance.route("/news/<symbol>", methods=["GET"])
@auth
def news(symbol):
    try:
        googlenews = GoogleNews(lang='en', region="US",
                                period="1d", encode="utf-8")
        googlenews.get_news(symbol)
        data = googlenews.result()
        result = []
        for news in data:
            obj = {
                "date": news["date"] if news["date"] is not None else "",
                "link": news["link"] if news["link"] is not None else "",
                "img": news["img"] if news["img"] is not None else "",
                "title": news["title"] if news["title"] is not None else "",
            }
            result.append(obj)
        print(result, file=sys.stderr)
        return jsonify(result)
    except Exception as e:
        print(e)
