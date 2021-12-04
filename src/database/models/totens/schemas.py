from database.models.index import *
from database.models.inference import schemas

class TotenBase(BaseModel):
    name: str
    localization: str
    description: str


class TotenCreate(TotenBase):
    pass


class Toten(TotenBase):
    id: int
    detections: List[schemas.Inference] = []

    class Config:
        orm_mode = True