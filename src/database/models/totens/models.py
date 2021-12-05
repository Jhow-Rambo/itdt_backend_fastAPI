from src.database.models.index import *

class Toten(Base):
    __tablename__ = "totens"

    id = Column(Integer, unique=True, primary_key=True, index=True)
    name = Column(String, index=True)
    localization = Column(String)
    description = Column(String)

    detections = relationship("Inference", cascade="all, delete-orphan")