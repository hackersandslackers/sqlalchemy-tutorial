"""Perform JOIN queries on models with relationships."""
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User


def get_all_posts(session: Session, admin_user: User):
    """
    Fetch all posts belonging to an author user.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param admin_user: Author of blog posts.
    :type admin_user: User

    :return: None
    """
    posts = (
        session.query(Post)
        .join(User, Post.author_id == User.id)
        .filter_by(username=admin_user.username)
        .all()
    )
    for post in posts:
        post_record = {
            "post_id": post.id,
            "title": post.title,
            "summary": post.summary,
            "status": post.status,
            "feature_image": post.feature_image,
            "author": {
                "id": post.author_id,
                "username": post.author.username,
                "first_name": post.author.first_name,
                "last_name": post.author.last_name,
                "role": post.author.role,
            },
        }
        LOGGER.info(post_record)


def get_all_comments(session: Session):
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
