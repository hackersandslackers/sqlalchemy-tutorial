"""Create, delete and update records with SQLAlchemy's ORM."""
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part2_orm.models import User


def orm_create_user(session: Session, user: User) -> User:
    """
    Create a new instance of our `User` model.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param user: User data model for creation.
    :type user: User

    :return: User
    """
    try:
        session.add(user)  # Add the user
        session.commit()  # Commit the change
        LOGGER.success(f"Created new user: {user}")
        return user
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e


def orm_delete_user(session: Session, user: User):
    """
    Delete a user if it exists.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param user: User to be deleted.
    :type user: User

    :return: None
    """
    try:
        session.delete(user)  # Delete the user
        session.commit()  # Commit the change
        LOGGER.success(f"Deleted user: {user}")
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when deleting user: {e}")
        raise e
