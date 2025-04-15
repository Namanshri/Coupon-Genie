from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Coupon, Base
from database import engine, SessionLocal

from pydantic import BaseModel
from typing import List

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Dependency: Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for request and response
class CouponRequest(BaseModel):
    store: str
    discount: str
    category: str
    customer_segment: str
    predicted_success_rate: float

# POST endpoint to add a coupon
@app.post("/add-coupon/")
def add_coupon(coupon: CouponRequest, db: Session = Depends(get_db)):
    new_coupon = Coupon(**coupon.dict())
    db.add(new_coupon)
    db.commit()
    db.refresh(new_coupon)
    return new_coupon

# GET endpoint to retrieve all coupons
@app.get("/get-coupons/", response_model=List[CouponRequest])
def get_coupons(db: Session = Depends(get_db)):
    return db.query(Coupon).all()