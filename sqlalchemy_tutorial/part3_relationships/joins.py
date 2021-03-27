"""Perform JOIN queries on models with relationships."""
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Post


def get_posts(session: Session):
    """
    Fetch posts.

    :param session: SQLAlchemy database session.
    :type session: Session

    :return: None
    """
    posts = session.query(Post).all()
    for post in posts:
        LOGGER.info(f"Post: {post}")
        LOGGER.info(f"Post author: {post.author}")
