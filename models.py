from sqlalchemy import Boolean, Column, Integer, String, Float
from database import Base

class Lease(Base):
    __tablename__ = 'lease'

    Poster= Column(String, primary_key=True, index=True)
    Contact = Column(String(length=100))  # Specify length for VARCHAR column
    ImgId = Column(String(length=100))  # Specify length for VARCHAR column
    PropertyInfo = Column(String(length=255))  # Specify length for VARCHAR column
    Price = Column(Float)
    LeasePeriod = Column(String(length=50))  # Specify length for VARCHAR column
    PropertyName = Column(String(length=100))  # Specify length for VARCHAR column


