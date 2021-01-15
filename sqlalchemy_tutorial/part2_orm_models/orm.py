"""Create, delete and update records with SQLAlchemy's ORM."""
from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from sqlalchemy_tutorial.logger import LOGGER
from sqlalchemy_tutorial.part2_orm_models.models import User


def orm_create_user(session: Session) -> Optional[User]:
    """
    Create a new instance of our `User` model.

    :param session: SQLAlchemy database session.
    :type session: Session

    :returns: None
    """
    try:
        user = User(
            username="admin",
            password="Please don't set passwords like this",
            email="admin@example.com",
            first_name="Todd",
            last_name="Birchard",
            bio="I write tutorials on the internet.",
            avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
        )
        session.add(user)  # Add the user
        session.commit()  # Commit the change
        LOGGER.info(f"Created new user: {user}")
        return user
    except IntegrityError as e:
        LOGGER.error(e.orig)


def orm_delete_user(session: Session, user: User):
    """
    Delete a user if it exists.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param user: User created in the above function.
    :type user: User

    :returns: None
    """
    try:
        session.delete(user)  # Delete the user
        session.commit()  # Commit the change
        LOGGER.info(f"Deleted existing user: {user}")
    except IntegrityError as e:
        LOGGER.error(e.orig)
