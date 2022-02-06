from datetime import datetime
from db.database import connection
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from db.database import Base


class TickerInfos(Base):
    """
      table_name = ticker_infos
      info
      fiftyDayAverage
      fiftyTwoWeekHigh
      fiftyTwoWeekLow
      twoHundredDayAverage
      averageVolume10days
      averageVolume
      fiftyTwoWeekChange
      earningsGrowth
      earningsQuarterlyGrowth
      trailingPE
      trailingEps
    """

    __tablename__ = "ticker_infos"
    symbol = Column(String(150, 'utf8mb4_unicode_ci'),
                    primary_key=True, nullable=False)
    fiftyDayAverage = Column(Float)
    fiftyTwoWeekHigh = Column(Float)
    fiftyTwoWeekLow = Column(Float)
    twoHundredDayAverage = Column(Float)
    averageVolume10days = Column(Float)
    averageVolume = Column(Float)
    fiftyTwoWeekChange = Column(Float)
    earningsGrowth = Column(Float)
    earningsQuarterlyGrowth = Column(Float)
    trailingPE = Column(Float)
    trailingEps = Column(Float)

    def __init__(
            self,
            symbol,
            fiftyDayAverage,
            fiftyTwoWeekHigh,
            fiftyTwoWeekLow,
            twoHundredDayAverage,
            averageVolume10days,
            averageVolume,
            fiftyTwoWeekChange,
            earningsGrowth,
            earningsQuarterlyGrowth,
            trailingPE,
            trailingEps):
        self.symbol = symbol
        self.fiftyDayAverage = fiftyDayAverage
        self.fiftyTwoWeekHigh = fiftyTwoWeekHigh
        self.fiftyTwoWeekLow = fiftyTwoWeekLow
        self.twoHundredDayAverage = twoHundredDayAverage
        self.averageVolume10days = averageVolume10days
        self.averageVolume = averageVolume
        self.fiftyTwoWeekChange = fiftyTwoWeekChange
        self.earningsGrowth = earningsGrowth
        self.earningsQuarterlyGrowth = earningsQuarterlyGrowth
        self.trailingPE = trailingPE
        self.trailingEps = trailingEps

    def __json__(self):
        return [
            'symbol',
            'fiftyDayAverage',
            'fiftyTwoWeekHigh',
            'fiftyTwoWeekLow',
            'twoHundredDayAverage',
            'averageVolume10days',
            'averageVolume',
            'fiftyTwoWeekChange',
            'earningsGrowth',
            'earningsQuarterlyGrowth',
            'trailingPE',
            'trailingEps'
        ]

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])
