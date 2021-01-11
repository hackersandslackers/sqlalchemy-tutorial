"""Demonstrate the SQLAlchemy ORM"""
from sqlalchemy_tutorial.database import session
from sqlalchemy_tutorial.database.models import User


def orm_create_user():
    """Create a new instance of our `User` model."""
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
