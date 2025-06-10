import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from sqlalchemy import Column, String, Float, Integer, DateTime
from backenddatabase import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    run_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)