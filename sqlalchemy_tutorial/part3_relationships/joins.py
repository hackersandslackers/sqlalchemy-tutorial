"""Perform JOIN queries on models with relationships."""
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User


def get_all_posts(session: Session, admin_user: User):
    """
    Fetch all posts belonging to an author user.

    :param Session session: SQLAlchemy database session.
    :param User admin_user: Author of blog posts.

    :return: None
    """
    LOGGER.info("Fetching posts with child comments...")
    posts = session.query(Post).join(User, Post.author_id == User.id).filter_by(username=admin_user.username).all()
    for post in posts:
        LOGGER.success(f"Fetched posts by user: {post}")


def get_all_comments(session: Session):
    """
    Fetch all comments and join with their parent posts.

    :param session: SQLAlchemy database session.
    :type session: Session

    :return: None
    """
    LOGGER.info("Joining comments with parent posts...")
    comments = session.query(Comment).join(Post, Post.id == Comment.post_id).all()
    for comment in comments:
        LOGGER.success(f"Joined comments with parent posts: {comment}")
