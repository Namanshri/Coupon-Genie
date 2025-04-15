from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coupon(Base):
    __tablename__ = "coupons"
    
    id = Column(Integer, primary_key=True, index=True)
    store = Column(String)
    discount = Column(String)
    category = Column(String)
    customer_segment = Column(String)
    predicted_success_rate = Column(Float)