from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class LeaseBase(BaseModel):
    Poster: str
    Contact: str
    ImgId: str
    PropertyInfo: str
    Price: float
    LeasePeriod: str
    PropertyName: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/leases", status_code=status.HTTP_201_CREATED)
async def create_lease(lease : LeaseBase, db: db_dependency):
        db_user = models.Lease(**lease.model_dump())
        db.add(lease)
        db.commit()   