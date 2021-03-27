"""Perform JOIN queries on models with relationships."""
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post


def list_all_comments(session: Session):
    """
    Fetch all comments and join with their parent posts.

    :param session: SQLAlchemy database session.
    :type session: Session

    :return: None
    """
    comments = session.query(Comment).join(Post, Post.id == Comment.post_id).all()
    for comment in comments:
        comment_record = {
            "comment_id": comment.id,
            "body_summary": f"{comment.body[:50]}...",
            "upvotes": comment.upvotes,
            "comment_author_id": comment.user_id,
            "post": {
                "slug": comment.post.slug,
                "title": comment.post.title,
                "post_author": comment.post.author.username,
            },
        }
        LOGGER.info(comment_record)
