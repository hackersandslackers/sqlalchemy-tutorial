"""Create records related to one another via SQLAlchemy's ORM."""
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User


def create_user(session: Session, user: User) -> User:
    """
    Create a new user if username isn't already taken.

    :param Session session: SQLAlchemy database session.
    :param User user: New user record to create.

    :return: Optional[User]
    """
    try:
        existing_user = session.query(User).filter(User.username == user.username).first()
        if existing_user is None:
            session.add(user)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created user: {user}")
        else:
            LOGGER.warning(f"Users already exists in database: {existing_user}")
        return session.query(User).filter(User.username == user.username).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e


def create_post(session: Session, post: Post) -> Post:
    """
    Create a post.

    :param Session session: SQLAlchemy database session.
    :param Post post: Blog post to be created.

    :return: Post
    """
    try:
        existing_post = session.query(Post).filter(Post.slug == post.slug).first()
        if existing_post is None:
            session.add(post)  # Add the post
            session.commit()  # Commit the change
            LOGGER.success(f"Created post {post} published by user {post.author.username}")
            return session.query(Post).filter(Post.slug == post.slug).first()
        LOGGER.warning(f"Post already exists in database: {post}")
        return existing_post
    except IntegrityError as e:
        LOGGER.error(f"IntegrityError error when creating user: {e}")
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError error when creating user: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")


def create_comment(session: Session, comment: Comment) -> Comment:
    """
    Create a comment posted by `regular_user` on `admin_user`'s post.

    :param Session session: SQLAlchemy database session.
    :param Comment comment: User comment left on published post.

    :return: Comment
    """
    try:
        session.add(comment)  # Add the Comment
        session.commit()  # Commit the change
        LOGGER.success(f"Created comment {comment} from user {comment.user.username}.")
        return comment
    except IntegrityError as e:
        LOGGER.error(f"IntegrityError error when creating user: {e}")
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError error when creating user: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
