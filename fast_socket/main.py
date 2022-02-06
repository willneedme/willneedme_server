from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.logger import logger
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import insert, JSON
from config import URL
from db.database import connection, session
from models.users import Users
from models.ticker_charts import TickerCharts
from models.ticker_infos import TickerInfos
from models.tickers import Tickers
from datetime import datetime, timedelta
import yfinance as yf
from yahoo_fin import stock_info, news, options
import sys
import math

app = FastAPI()


@app.get("/")
async def client(request: Request):
    return "test"


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        # while True:
        symbols = await websocket.receive_json()  # symbols
        for symbol in symbols:
            ticker = yf.Ticker(symbol['symbol']).history(period="5d")
            reset = ticker.reset_index()
            history = reset.to_dict("records")
            for data in history:
                temp = insert(TickerCharts).values(
                    symbol=symbol['symbol'],
                    close=0 if math.isnan(
                        data["Close"]) else data["Close"],
                    high=0 if math.isnan(data["High"]) else data["High"],
                    open=0 if math.isnan(data["Open"]) else data["Open"],
                    low=0 if math.isnan(data["Low"]) else data["Low"],
                    volume=0 if math.isnan(
                        data["Volume"]) else data["Volume"],
                    date=datetime.strptime(
                        str(data["Date"]), '%Y-%m-%d %H:%M:%S'),
                    symbolDate=f"{symbol['symbol']}{data['Date']}"
                ).on_duplicate_key_update(
                    close=0 if math.isnan(
                        data["Close"]) else data["Close"],
                    high=0 if math.isnan(data["High"]) else data["High"],
                    open=0 if math.isnan(data["Open"]) else data["Open"],
                    low=0 if math.isnan(data["Low"]) else data["Low"],
                    volume=0 if math.isnan(
                        data["Volume"]) else data["Volume"],
                )
            session.execute(temp)
        session.commit()
        # filter_after = datetime.today() - timedelta(days=2)
        tickers = session.query(
            Tickers.symbol,
            Tickers.name,
            Tickers.country,
            Tickers.industry,
            Tickers.ipoYear,
            Tickers.logoUrl,
            Tickers.marketCap,
            Tickers.netChange,
            Tickers.sector,
            TickerInfos.symbol,
            TickerInfos.fiftyDayAverage,
            TickerInfos.fiftyTwoWeekChange,
            TickerInfos.fiftyTwoWeekHigh,
            TickerInfos.fiftyTwoWeekLow)\
            .join(TickerInfos, Tickers.symbol == TickerInfos.symbol)\
            .order_by(Tickers.marketCap.desc()).limit(len(symbols))

        tickers_result = [dict(row) for row in tickers]
        for ticker in tickers_result:
            t = session.query(
                TickerCharts.date,
                TickerCharts.close,
                TickerCharts.open,
                TickerCharts.high,
                TickerCharts.low,
                TickerCharts.volume
            ).filter(TickerCharts.symbol == ticker['symbol'])\
                .order_by(TickerCharts.date.desc()).limit(2)
            if t is not None:
                charts_result = [dict(row) for row in t]
                ticker["charts"] = charts_result
        json = jsonable_encoder(tickers_result)
        await websocket.send_json(json)
    except Exception as e:
        session.rollback()
        print(e, file=sys.stderr)


@app.websocket("/toplosers")
async def toplosers(websocket: WebSocket):
    try:
        await websocket.accept()
        data = stock_info.get_day_losers().reset_index().to_dict("records")
        result = []
        for ticker in data:
            # today = stock_info.get_live_price(ticker["Symbol"])
            obj = {
                "percent": ticker["% Change"],
                "marketCap": ticker["Market Cap"],
                "symbol": ticker["Symbol"],
                "price": ticker["Price (Intraday)"],
                # "today": today
            }
            # print(obj, file=sys.stderr)
            result.append(obj)
        json = jsonable_encoder(result)
        await websocket.send_json(json)
    except Exception as e:
        session.rollback()
        print("toplose{}".format(e), file=sys.stderr)
