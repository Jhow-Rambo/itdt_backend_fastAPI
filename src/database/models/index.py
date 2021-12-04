from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.settings import Base

from typing import List, Optional
from fastapi import HTTPException

from pydantic import BaseModel, validator