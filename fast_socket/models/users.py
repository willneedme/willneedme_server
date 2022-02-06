from datetime import datetime
from db.database import connection
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from db.database import Base


class Users(Base):
    """
      uid
      displayName
      email
      emailVerified
      phoneNumber
      deviceToken
      receiveFcm
      isAdmin
      createdAt
      updatedAt
      loginType
    """

    __tablename__ = "users"

    uid = Column(String(100, 'utf8mb4_unicode_ci'),
                 primary_key=True, nullable=False,)
    displayName = Column(String(200, 'utf8mb4_unicode_ci'))
    email = Column(String(200, 'utf8mb4_unicode_ci'))
    emailVerified = Column(Boolean)
    phoneNumber = Column(String(50))
    deviceToken = Column(Text)
    receiveFcm = Column(Boolean)
    isAdmin = Column(Boolean)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    loginType = Column(String(20, 'utf8mb4_unicode_ci'))

    def __init__(self, uid, displayName, email, emailVerified, phoneNumber, deviceToken, receiveFcm, isAdmin, createdAt, updatedAt, loginType):
        self.uid = uid
        self.displayName = displayName
        self.email = email
        self.emailVerified = emailVerified
        self.phoneNumber = phoneNumber
        self.deviceToken = deviceToken
        self.receiveFcm = receiveFcm
        self.isAdmin = isAdmin
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.loginType = loginType

    def __repr__(self):
        return f"AdminUser('{self.adminEmail}','{self.adminName}','{self.adminPassword}','{self.connectTime}')"
