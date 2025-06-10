from sqlalchemy.orm import Session
from backendmodels import User
from datetime import datetime
from sqlalchemy import func

def save_users(db: Session, users: list, run_id: int):
    for u in users:
        db_user = User(
            uid=u["uid"],
            email=u["email"],
            first_name=u["first_name"],
            last_name=u["last_name"],
            gender=u["gender"],
            latitude=u["latitude"],
            longitude=u["longitude"],
            run_id=run_id,
            created_at=datetime.utcnow()
        )
        db.add(db_user)
    db.commit()

def get_random_user(db: Session):
    return db.query(User).order_by(func.random()).first()

def get_user_by_uid(db: Session, uid: str):
    return db.query(User).filter(User.uid == uid).first()

def get_nearest_users(db: Session, uid: str, limit: int = 100):
    user = get_user_by_uid(db, uid)
    if not user:
        return []

    lat, lon = user.latitude, user.longitude
    return db.query(User).filter(User.uid != uid).order_by(
        func.abs(User.latitude - lat) + func.abs(User.longitude - lon)
    ).limit(limit).all()
