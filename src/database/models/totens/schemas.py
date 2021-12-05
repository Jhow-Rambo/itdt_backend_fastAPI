from src.database.models.index import *
from src.database.models.inference import schemas

class TotenBase(BaseModel):
    name: str
    localization: str
    description: str



class TotenCreate(TotenBase):
    @validator('*',  pre=True, always=True)
    def must_be_provided(cls, v, field):
        if v == '':
            raise HTTPException(status_code=400, detail=f"{field.name} must be provided")
        else:
            return v.title()

class Toten(TotenBase):
    id: int
    detections: List[schemas.Inference] = []

    class Config:
        orm_mode = True