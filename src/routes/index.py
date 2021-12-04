# from ..main import get_db
from services.inference import InferenceService
from services.toten import TotenService
from config.settings import SessionLocal, engine
# from database.models import models, schemas
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db

router = APIRouter()
