# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db.database import connection
from sqlalchemy import Column, Integer, String, DateTime
# db = SQLAlchemy()
from db.database import Base


class AdminUser(Base):
    """
      table name = adminUser
      info
      id
      adminEmail
      adminName
      adminPassword
      connectTime
      connectIp
    """

    __tablename__ = "willneedme_user"
    # __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    adminEmail = Column(String(100, 'utf8mb4_unicode_ci'))
    adminName = Column(String(20, 'utf8mb4_unicode_ci'))
    adminPassword = Column(String(40, 'utf8mb4_unicode_ci'))
    connectTime = Column(DateTime, default=datetime.utcnow())
    connectIp = Column(String(30))

    def __init__(self, adminEmail, adminName, adminPassword, connectTime, connectIp):
        self.adminEmail = adminEmail
        self.adminName = adminName
        self.adminPassword = adminPassword
        self.connectTime = connectTime
        self.connectIp = connectIp

    def __repr__(self):
        return f"AdminUser('{self.adminEmail}','{self.adminName}','{self.adminPassword}','{self.connectTime}')"
