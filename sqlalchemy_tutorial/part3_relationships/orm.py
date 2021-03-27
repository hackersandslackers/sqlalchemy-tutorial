"""Create records related to one another via SQLAlchemy's ORM."""
from typing import Tuple

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User


def create_users(
    session: Session, admin_user: User, regular_user: User
) -> Tuple[User, User]:
    """
    Create a couple of user accounts.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param admin_user: User model representing admin user to be created.
    :type admin_user: User
    :param regular_user: User model representing non-admin user to be created.
    :type regular_user: User

    :return: Tuple[User, User]
    """
    admin_user = create_new_user(session, admin_user)
    regular_user = create_new_user(session, regular_user)
    LOGGER.success(f"Created 2 users: {admin_user} & {regular_user}")
    return admin_user, regular_user


def create_new_user(session: Session, user: User) -> User:
    """
    Create a new user if username isn't already taken.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param user: New user record to create.
    :type user: User

    :return: Optional[User]
    """
    try:
        user_query = session.query(User).filter(User.username == user.username).first()
        if user_query is None:
            session.add(user)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created user: {user}")
        else:
            LOGGER.warning(f"Users already exists in database: {user_query}")
        return session.query(User).filter(User.username == user.username).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e


def create_post(session: Session, post: Post, admin_user: User) -> Post:
    """
    Create a post authored by `admin_user`.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param post: Blog post to be created.
    :type post: Post
    :param admin_user: User to serve as post author.
    :type admin_user: User

    :return: Post
    """
    try:
        existing_post = (
            session.query(Post).filter(Post.author_id == admin_user.id).first()
        )
        if existing_post is None:
            post.author_id = admin_user.id
            session.add(post)  # Add the post
            session.commit()  # Commit the change
            LOGGER.success(
                f"Created post {post} published by user {admin_user.username}"
            )
            return session.query(Post).filter(Post.author_id == admin_user.id).first()
        else:
            LOGGER.warning(f"Post already exists in database: {post}")
            return existing_post
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e


def create_comment(session: Session, regular_user: User, post: Post) -> Comment:
    """
    Create a comment posted by `regular_user` on `admin_user`'s post.

    :param session: SQLAlchemy database session.
    :type session: Session
    :param regular_user: User to serve as comment author.
    :type regular_user: User
    :param post: Blog post to be commented on.
    :type post: Post

    :return: Comment
    """
    try:
        comment = Comment(
            user_id=regular_user.id,
            post_id=post.id,
            body="This post about SQLAlchemy is awful. You didn't even bother to explain how to install Python, \
                            which is where I (and so many others) got stuck. Plus, your code doesn't even work!! \
                            I cloned your code and it keeps giving me `environment variable` errors... \
                            WTF are environment variables?!!?!?",
            upvotes=2,
        )
        session.add(comment)  # Add the Comment
        session.commit()  # Commit the change
        LOGGER.success(f"Created comment {comment} posted by user {regular_user}")
        return comment
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating comment: {e}")
        raise e
