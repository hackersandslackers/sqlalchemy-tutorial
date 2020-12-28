"""Create database connection."""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import SQLALCHEMY_DATABASE_URI

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Create database session
session = Session(engine)
