import requests
import pandas as pd
from flask import Blueprint, jsonify, request
import yfinance as yf
import numpy as np
import sys
import pymysql
import os
import json
import pymysql
from yahoo_fin import stock_info, news, options
from sqlalchemy.dialects.mysql import insert, JSON
from sqlalchemy.orm import class_mapper
from sqlalchemy import and_, or_, func
from datetime import datetime, timedelta
from models.adminUser import AdminUser
from models.tickers import Tickers
from models.ticker_charts import TickerCharts
from models.ticker_infos import TickerInfos
from db.database import connection, session
from utils.nasdaq import Nasdaq
from utils.date import yearMonthDay
from middleware.auth import auth

analyze = Blueprint("analyze", __name__)


@analyze.route("/toplosers", methods=["GET"])
@auth
def toplosers():
    try:
        data = stock_info.get_day_losers().reset_index().to_dict("records")
        result = []
        for ticker in data:
            # today = stock_info.get_live_price(ticker["Symbol"])
            if type(ticker["Market Cap"]) is str:
                ticker["Market Cap"] = float(
                    ticker["Market Cap"].replace("T", "")) * 1000000000000
            obj = {
                "percent": ticker["% Change"],
                "marketCap": ticker["Market Cap"],
                "symbol": ticker["Symbol"],
                "price": ticker["Price (Intraday)"],
                # "today": today
            }
            # print(obj, file=sys.stderr)
            result.append(obj)
        return jsonify(result)
    except Exception as e:
        print(e, file=sys.stderr)
        return jsonify(str(e))


@analyze.route("/topgainers", methods=["GET"])
@auth
def topgainers():
    try:
        data = stock_info.get_day_gainers().reset_index().to_dict("records")
        result = []
        for ticker in data:
            if type(ticker["Market Cap"]) is str:
                ticker["Market Cap"] = float(
                    ticker["Market Cap"].replace("T", "")) * 1000000000000
            obj = {
                "percent": ticker["% Change"],
                "marketCap": ticker["Market Cap"],
                "symbol": ticker["Symbol"],
                "price": ticker["Price (Intraday)"],
                # "today": today
            }
            result.append(obj)
        return jsonify(result)
    except Exception as e:
        print(e, file=sys.stderr)
        return jsonify(None)


@analyze.route("/test", methods=["GET"])
@auth
def test():
    data = stock_info.get_stats("AAPL").reset_index().to_dict("records")
    return jsonify(data)


@analyze.route("/fiftytwolow", methods=["GET"])
@auth
def fiftytwolow():
    try:
        return jsonify(None)
        fiftytwolow = session.query()
    except Exception as e:
        print(e, file=sys.stderr)
        return jsonify(None)


@analyze.route("/fiftytwohigh", methods=["GET"])
@auth
def fiftytwohigh():
    try:
        return jsonify(None)
        fiftytwohigh = session.query()
    except Exception as e:
        print(e, file=sys.stderr)
        return jsonify(None)
