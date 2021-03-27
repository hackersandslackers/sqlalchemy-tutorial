"""Database config."""
from os import environ, path

from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Database connection variables
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_DATABASE_PEM = environ.get("SQLALCHEMY_DATABASE_PEM")

# Reset data after each run
CLEANUP_DATA = True
