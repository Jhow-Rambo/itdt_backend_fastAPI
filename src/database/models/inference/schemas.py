from src.database.models.index import *


class InferenceBase(BaseModel):
    inference: str
    inferred_image: str
    normal_image: str


class InferenceCreate(InferenceBase):
    @validator('*',  pre=True, always=True)
    def must_be_provided(cls, v, field):
        if v == '':
            raise HTTPException(status_code=400, detail=f"{field.name} must be provided")
        else:
            return v.title()




class Inference(InferenceBase):
    id: int
    # toten_id: int

    class Config:
        orm_mode = True