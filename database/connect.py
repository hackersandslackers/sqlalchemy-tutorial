"""Create SQLAlchemy engine and session objects."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_PEM, SQLALCHEMY_DATABASE_URI

# Create database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"ssl": {"key": SQLALCHEMY_DATABASE_PEM}}
)

# Create database session
Session = sessionmaker(bind=engine)
session = Session()
