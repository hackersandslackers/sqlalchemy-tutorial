from database import session
from sqlalchemy_tutorial.part2_orm.models import User

from .orm import orm_create_user, orm_delete_user


def create_and_delete_users():
    """
    Create a user record via SQLAlchemy's ORM, and subsequently delete it.

    :return: None
    """
    user = User(
        username="admin",
        password="Password123lol",
        email="admin@example.com",
        first_name="Todd",
        last_name="Birchard",
        bio="I write tutorials on the internet.",
        avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
    )
    user = orm_create_user(session, user)
    orm_delete_user(session, user)
