
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.models import HeadOfSpecifications
from app.database import SessionLocal


class AccessService:
    def __init__(self, db: Session):
        self.db = db

    def SpecificationFind(self, article: int) -> List[HeadOfSpecifications]:
        return self.db.query(HeadOfSpecifications).filter(
            HeadOfSpecifications.KA2450_REZ_NR == article 
        ).first()



