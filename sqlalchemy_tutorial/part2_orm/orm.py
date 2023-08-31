"""Create, delete and update records with SQLAlchemy's ORM."""
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part2_orm.models import User


def orm_create_user(session: Session, user: User) -> User:
    """
    Create a new instance of our `User` model.

    :param Session session: SQLAlchemy database session.
    :param User user: User data model for creation.

    :return: User
    """
    try:
        session.add(user)  # Add the user
        session.commit()  # Commit the change
        LOGGER.success(f"Created new user: {user}")
        return user
    except IntegrityError as e:
        LOGGER.error(f"IntegrityError when creating user: {e}")
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError when creating user: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")


def orm_delete_user(session: Session, user: User):
    """
    Delete a user if it exists.

    :param Session session: SQLAlchemy database session.
    :param User user: User to be deleted.

    :return: None
    """
    try:
        session.delete(user)  # Delete the user
        session.commit()  # Commit the change
        LOGGER.success(f"Deleted user: {user}")
    except IntegrityError as e:
        LOGGER.error(f"IntegrityError when deleting user: {e}")
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError when deleting user: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when deleting user: {e}")
