"""Purge all data from database."""
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import session
from logger import LOGGER


def cleanup_data():
    """Purge test database of all data."""
    try:
        session.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
        session.commit()
        session.execute(text("TRUNCATE TABLE comment;"))
        session.commit()
        session.execute(text("TRUNCATE TABLE post;"))
        session.commit()
        session.execute(text("TRUNCATE TABLE user;"))
        session.commit()
        session.execute(text("SET FOREIGN_KEY_CHECKS=1;"))
        session.commit()
        LOGGER.success("Successfully reset all data.")
    except IntegrityError as e:
        LOGGER.error(f"Integrity error when resetting data: {e}")
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError error when resetting data: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when resetting data: {e}")
