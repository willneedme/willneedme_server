from datetime import datetime
from db.database import connection
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from db.database import Base


class TickerCharts(Base):
    """
      table name = ticker_charts
      info
      date
      symbol
      close
      high
      low
      open
      volume
      symbolDate
    """

    __tablename__ = "ticker_charts"

    date = Column(DateTime)
    symbol = Column(String(150, 'utf8mb4_unicode_ci'))
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    volume = Column(Integer)
    symbolDate = Column(String(180, 'utf8mb4_unicode_ci'), primary_key=True,
                        nullable=False)

    def __init__(self, symbol, date, close, high, low, open, volume, symbolDate):
        self.symbol = symbol
        self.date = date
        self.close = close
        self.high = high
        self.low = low
        self.open = open
        self.volume = volume
        self.symbolDate = symbolDate

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])
