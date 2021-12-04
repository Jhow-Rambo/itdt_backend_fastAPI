from ..index import *
from database.models.totens import models, schemas 

@router.get("/toten/{id}", response_model=schemas.Toten)
async def read_totens(id: int, db: Session = Depends(get_db)):
    return totens.get_totens_by_id(db, id)

@router.get("/toten", response_model=List[schemas.Toten])
async def read_totens(db: Session = Depends(get_db)):
    allTotens = totens.get_totens(db)
    return allTotens

@router.post("/toten", response_model=schemas.TotenCreate)
async def create_totens(toten: schemas.TotenCreate, db: Session = Depends(get_db)):
    return totens.create_toten(db, toten)

@router.delete("/toten/{id}")
async def delete_totens(id: int, db: Session = Depends(get_db)):
    return totens.delete_totens(db, id)