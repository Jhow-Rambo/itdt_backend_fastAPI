from ..index import *
from database.models.inference import models, schemas 

@router.post("/inference/{toten_id}", response_model=schemas.InferenceCreate)
async def create_toten_inference(toten_id: int, inferenceData: schemas.InferenceCreate, db: Session = Depends(get_db)):
    return InferenceService.create_inference(db, inferenceData, toten_id)

@router.get("/inference", response_model=List[schemas.Inference])
async def get_inferences(db: Session = Depends(get_db)):
    allInferences = InferenceService.get_inferences(db)
    return allInferences
