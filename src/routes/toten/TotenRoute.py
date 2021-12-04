from ..index import *
from fastapi import HTTPException
from database.models.totens import models, schemas 

@router.get("/toten/{id}", response_model=schemas.Toten)
async def read_one_toten(id: int, db: Session = Depends(get_db)):
    return TotenService.get_totens_by_id(db, id)

@router.get("/toten", response_model=List[schemas.Toten])
async def read_totens(db: Session = Depends(get_db)):
    allTotens = TotenService.get_totens(db)
    return allTotens

@router.post("/toten", response_model=schemas.TotenCreate, status_code=201)
async def create_totens(toten: schemas.TotenCreate, db: Session = Depends(get_db)):
    return TotenService.create_toten(db, toten)

@router.delete("/toten/{id}")
async def delete_totens(id: int, db: Session = Depends(get_db)):
    return TotenService.delete_totens(db, id)