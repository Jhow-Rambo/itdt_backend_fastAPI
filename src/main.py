from fastapi import FastAPI
import uvicorn


from database.models.totens import models as totenModel
from database.models.inference import models as inferenceModel
from routes.inference import inference
from routes.toten import toten
from config.settings import SessionLocal, engine

totenModel.Base.metadata.create_all(bind=engine)
inferenceModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(inference.router)
app.include_router(toten.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    # print(__package__)
    uvicorn.run(app, host="127.0.0.1", port=3000)