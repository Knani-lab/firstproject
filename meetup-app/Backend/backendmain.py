from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database, crud, utils
import random

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Meetup API is running."}

@app.post("/populate")
def populate_users(db: Session = Depends(get_db)):
    users = utils.fetch_random_users()
    for user_data in users:
        crud.create_user(db, user_data)
    return {"message": f"{len(users)} users added."}

@app.get("/closest")
def get_closest_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    if not users:
        return {"message": "No users found."}
    reference = random.choice(users)
    closest = utils.find_closest_users(reference, users)
    return {
        "reference_user": {
            "id": reference.id,
            "name": reference.name,
            "email": reference.email,
        },
        "closest_users": [{"name": u.name, "email": u.email, "latitude": u.latitude, "longitude": u.longitude} for u in closest]
    }

