from sqlalchemy import and_
from sqlalchemy.orm import Session

from db import models

class Admins:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all_admins(self) -> list[models.Admins]:
        return self.db.query(models.Admins).all()
    
    def get_admins_filtered(self, name: str, email: str) -> list[models.Admins]:
        filters = []
        if name: filters.append(models.Admins.name == name)
        if email: filters.append(models.Admins.email == email)
        return self.db.query(models.Admins).filter(and_(*filters)).order_by(models.Admins.id.desc()).all()