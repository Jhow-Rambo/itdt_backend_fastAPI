from ..index import *
from database.models.inference import models, schemas 

def create_inference(db: Session, inference: schemas.InferenceCreate, toten_id: int):
    db_inference = models.Inference(**inference.dict(), toten_id=toten_id)
    db.add(db_inference)
    db.commit()
    db.refresh(db_inference)
    return inference

def get_inferences(db: Session):
    db_inferences = db.query(models.Inference).all()
    return db_inferences