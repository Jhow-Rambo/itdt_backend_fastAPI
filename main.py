from fastapi import FastAPI
import uvicorn


from src.database.models.totens import models as totenModel
from src.database.models.inference import models as inferenceModel
from src.routes.inference import InferenceRoute
from src.routes.toten import TotenRoute
from src.config.settings import SessionLocal, engine

totenModel.Base.metadata.create_all(bind=engine)
inferenceModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(InferenceRoute.router)
app.include_router(TotenRoute.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
async def root():
    return {"message": "Hello World"}

# if __name__ == "__main__":
#     # print(__package__)
#     uvicorn.run(app, host="127.0.0.1", port=3000)