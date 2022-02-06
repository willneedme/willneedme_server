from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.logger import logger
from db.database import connection
from sqlalchemy import create_engine
from config import URL, config
import os
import sys
import eventlet

eventlet.monkey_patch()
app = FastAPI()
engine = create_engine(URL, echo=False)


def create_app():
    app.config.from_pyfile("config.py")
    app.config["SECRET_KEY"] = os.environ["AUTH_TOKEN"]
    app.database = engine

    return app


socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@app.route("/", methods=["GET"])
def defaultRoute():
    emit("message", "test")
    return redirect("http://willneedme.com")
