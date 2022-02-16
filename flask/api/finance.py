from flask import Blueprint, jsonify, request
from utils.date import yearMonthDay
from middleware.auth import auth
import FinanceDataReader as fdr
from datetime import datetime, timedelta
import sys
import pandas as pd
import numpy as np
# test
import math
from utils.nasdaq import Nasdaq
from db.database import session
from models.tickers import Tickers
from sqlalchemy.dialects.mysql import insert
from yahoo_fin import stock_info, news, options

finance = Blueprint("finance", __name__)

# 심볼	설명
# KS11	KOSPI 지수
# KQ11	KOSDAQ 지수
# KS50	KOSPI 50 지수
# KS100 KOSPI 100
# DJI	다우존스 지수
# IXIC	나스닥 지수
# US500 S & P 500 지수
# JP225	닛케이 225 선물
# STOXX50E	Euro Stoxx 50
# CSI300	CSI 300 (중국)
# HSI	항셍 (홍콩)
# FTSE	영국 FTSE
# DAX	독일 DAX 30
# CAC	프랑스 CAC 40


@finance.route("/index/kospi", methods=["GET"])
@auth
def default():
    # index = ["KS11", "KQ11", "IXIC", "DJI"]
    try:
        index = fdr.DataReader("KS11", yearMonthDay(-30)).reset_index()
        kospi = index.rename(columns={"Close": "close", "Date": "date",
                                      "Open": "open", "High": "high", "Low": "low", "Volume": "volume"}).to_dict("records")
        for row in kospi:
            row["date"] = row["date"].isoformat()

        return jsonify(kospi)
    except Exception as e:
        return jsonify(None)


@finance.route("/index/kosdaq", methods=["GET"])
@auth
def kosdaq():
    # index = ["KS11", "KQ11", "IXIC", "DJI"]
    try:
        index = fdr.DataReader("KQ11", yearMonthDay(-30)).reset_index()
        kosdaq = index.rename(columns={"Close": "close", "Date": "date",
                                       "Open": "open", "High": "high", "Low": "low", "Volume": "volume"}).to_dict("records")
        for row in kosdaq:
            row["date"] = row["date"].isoformat()

        return jsonify(kosdaq)
    except Exception as e:
        return jsonify(None)


@finance.route("/index/nasdaq", methods=["GET"])
@auth
def nasdaq():
    # index = ["KS11", "KQ11", "IXIC", "DJI"]
    try:
        index = fdr.DataReader("IXIC", yearMonthDay(-30)).reset_index()
        nasdaq = index.rename(columns={"Close": "close", "Date": "date",
                                       "Open": "open", "High": "high", "Low": "low", "Volume": "volume"}).to_dict("records")
        for row in nasdaq:
            row["date"] = row["date"].isoformat()

        return jsonify(nasdaq)
    except Exception as e:
        return jsonify(None)


@finance.route("/index/dowjones", methods=["GET"])
@auth
def downjones():
    # index = ["KS11", "KQ11", "IXIC", "DJI"]
    try:
        index = fdr.DataReader("KS11", yearMonthDay(-30)).reset_index()
        downjones = index.rename(columns={"Close": "close", "Date": "date",
                                          "Open": "open", "High": "high", "Low": "low", "Volume": "volume"}).to_dict("records")
        for row in downjones:
            row["date"] = row["date"].isoformat()

        return jsonify(downjones)
    except Exception as e:
        return jsonify(None)


@finance.route("/test", methods=["GET"])
def test():
    ticker = session.query(Tickers.name, Tickers.industry, Tickers.sector, Tickers.netChange)\
        .filter(Tickers.symbol == "005930").first()

    obj = {
        "logoUrl": None,
        "industry": ticker["industry"] if ticker is not None else "",
        "sector": ticker["sector"] if ticker is not None else "",
        "netChange": ticker["netChange"] if ticker is not None else 0,
        "name": ticker["name"],
        "averageVolumeThreeMonth": None,
        "averageVolumeTenDay": None,
        "fiftyDayAverage": None,
        "fiftyTwoWeekHigh": None,
        "fiftyTwoWeekLow": None,
        "marketCap": None,
        "symbol": None,
        "trailingPE": None,
        "twoHundredDayAverage": None
    }
    charts = fdr.DataReader("005930").reset_index()\
        .rename(columns={"Close": "close", "Date": "date",
                         "Open": "open", "High": "high", "Low": "low", "Volume": "volume"}).to_dict("records")

    for row in charts:
        row["date"] = row["date"].isoformat()
    result = [row for row in charts if math.isnan(
        row['open']) is False]
    # sortedChart = sorted(charts, key=(lambda x: x['date']), reverse=True)
    obj["charts"] = result
    return jsonify(obj)
