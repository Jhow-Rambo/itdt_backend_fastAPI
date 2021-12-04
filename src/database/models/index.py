from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.settings import Base

from typing import List, Optional

from pydantic import BaseModel