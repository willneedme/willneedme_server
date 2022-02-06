from flask import Flask
from db.database import connection
from sqlalchemy import create_engine
from config import URL, config

app = Flask(__name__)


def create_app():
    app.config.from_pyfile("config.py")
    return app
