"""Database config."""
from os import getenv, path

from dotenv import load_dotenv

# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# Database connection variables
DATABASE_USERNAME = getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = getenv("DATABASE_PASSWORD")
DATABASE_HOST = getenv("DATABASE_HOST")
DATABASE_PORT = getenv("DATABASE_PORT")
DATABASE_TABLE = getenv("DATABASE_TABLE")
DATABASE_CERT_FILE = getenv("DATABASE_CERT_FILE")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_TABLE}?ssl_ca={DATABASE_CERT_FILE}"

# Reset data after each run
CLEANUP_DATA = False
