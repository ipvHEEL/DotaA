from fastapi import FastAPI, Depends 
# from sqlalchemy.orm import Session  
# from app.database import get_db
# from app.service.access import AccessService

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Service is running"}


