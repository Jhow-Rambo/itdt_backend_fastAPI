from database.models.index import *


class InferenceBase(BaseModel):
    inference: str
    inferred_image: str
    normal_image: str


class InferenceCreate(InferenceBase):
    pass


class Inference(InferenceBase):
    id: int
    # toten_id: int

    class Config:
        orm_mode = True