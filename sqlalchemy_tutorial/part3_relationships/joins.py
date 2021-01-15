"""Perform JOIN queries on models with relationships."""
from sqlalchemy.orm import Session

from sqlalchemy_tutorial.logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User


def get_posts(session: Session):
    """
    Fetch posts.

    :returns: None
    """
    posts = session.query(Post).all()
    for post in posts:
        LOGGER.info(f"Post: {post}")
        LOGGER.info(f"Post author: {post.author}")
