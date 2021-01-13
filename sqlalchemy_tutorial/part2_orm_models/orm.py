"""Create, delete and update records with SQLAlchemy's ORM."""
from sqlalchemy.orm import Session

from sqlalchemy_tutorial.logger import LOGGER
from sqlalchemy_tutorial.part2_orm_models.models import User

# Define instance of our `User` model
user = User(
    username="admin",
    password="Please don't set passwords like this",
    email="admin@example.com",
    first_name="Todd",
    last_name="Birchard",
    bio="I write tutorials on the internet.",
    avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
)


def orm_create_user(session: Session):
    """
    Create a new instance of our `User` model.

    :param session: SQLAlchemy database session.
    :type session: Session

    :returns: None
    """
    session.add(user)  # Add the user
    session.commit()  # Commit the change

    LOGGER.info(f"Create new user: {user}")


def orm_delete_user(session: Session):
    """
    Delete a user if it exists.

    :param session: SQLAlchemy database session.
    :type session: Session

    :returns: None
    """
    session.delete(user)  # Delete the user
    session.commit()  # Commit the change

    LOGGER.info(f"Deleted existing user: {user}")
