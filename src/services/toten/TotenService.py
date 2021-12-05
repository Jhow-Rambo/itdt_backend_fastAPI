from ..index import *
from src.database.models.totens import models, schemas
from src.database.models.inference.models import Inference

def create_toten(db: Session, toten: schemas.TotenCreate):
    db_toten = models.Toten(name=toten.name, localization=toten.localization, description=toten.description)
    db.add(db_toten)
    db.commit()
    db.refresh(db_toten)
    return toten

def get_totens(db: Session):
    db_totens = db.query(models.Toten).all()
    # db_totens = db.query(models.Toten).join(Inference).all()
    return db_totens

def get_totens_by_id(db: Session, id):
    db_toten = db.query(models.Toten).filter(models.Toten.id == id).first()
    return db_toten

def delete_totens(db: Session, id):
    print('entrou')
    db_toten = db.query(models.Toten).filter(models.Toten.id == id).first()
    db.delete(db_toten)
    db.commit()
