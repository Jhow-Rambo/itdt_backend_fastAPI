from database.models.index import *


class Inference(Base):
    __tablename__ = "inferences"

    id = Column(Integer, primary_key=True, index=True)
    inference = Column(String, index=True)
    inferred_image = Column(String, index=True)
    normal_image = Column(String, index=True)
    toten_id = Column(Integer, ForeignKey("totens.id"))

    # owner = relationship("Toten", back_populates="detections")