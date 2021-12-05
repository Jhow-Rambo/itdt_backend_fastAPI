# from ..main import get_db
from src.services.inference import InferenceService
from src.services.toten import TotenService
from src.config.settings import SessionLocal, engine
# from database.models import models, schemas
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends
from src.database.database import get_db

router = APIRouter()
