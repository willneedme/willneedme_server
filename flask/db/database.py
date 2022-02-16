from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import mariadb
import pymysql
import os
from config import config, URL

engine = create_engine(URL, pool_pre_ping=True)
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = session.query_property()
Base.metadata.create_all(engine)


def connection():
    conn = pymysql.connect(**config)
    return conn
