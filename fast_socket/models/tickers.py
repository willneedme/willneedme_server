from datetime import datetime
from db.database import connection
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from db.database import Base


class Tickers(Base):
    """
      table name = tickers
      info
      symbol
      country
      industry
      ipoYear
      sector
      marketCap
      name
      netChange
      logoUrl
    """

    __tablename__ = "tickers"

    symbol = Column(String(150), primary_key=True,
                    nullable=False)
    country = Column(String(100, 'utf8mb4_unicode_ci'))
    industry = Column(String(200, 'utf8mb4_unicode_ci'))
    ipoYear = Column(String(10))
    sector = Column(String(100, 'utf8mb4_unicode_ci'))
    marketCap = Column(Float)
    name = Column(String(250, 'utf8mb4_unicode_ci'))
    netChange = Column(Float)
    logoUrl = Column(Text)

    def __init__(self, symbol, country, industry, ipoYear, sector, marketCap, name, netChange, logoUrl):
        self.symbol = symbol
        self.country = country
        self.industry = industry
        self.ipoYear = ipoYear
        self.sector = sector
        self.marketCap = marketCap
        self.name = name
        self.netChange = netChange
        self.logoUrl = logoUrl

    def __json__(self):
        return [
            'symbol',
            'country',
            'industry',
            'ipoYear',
            'sector',
            'marketCap',
            'name',
            'netChange',
            'logoUrl'
        ]

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])
