"""Create records from our data models with SQLAlchemy's ORM."""
from typing import Tuple

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from sqlalchemy_tutorial.logger import LOGGER
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User


def orm_create_data(session: Session) -> None:
    """
    Populate our database with users, posts, and comments to query on.

    :param session: SQLAlchemy database session.
    :type session: Session

    :returns: None
    """
    create_users(session)
    create_post(session)
    create_comment(session)
    LOGGER.info(f"Finished creating user, post, and comment records.")


def create_users(session: Session) -> Tuple[User, User]:
    """
    Create a couple of user accounts.

    :param session: SQLAlchemy database session.
    :type session: Session

    :returns: Tuple[User, User]
    """
    admin_user = User(
        username="toddthebod",
        password="Please don't set passwords like this",
        email="todd@example.com",
        first_name="Todd",
        last_name="Birchard",
        bio="I write tutorials on the internet.",
        avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
        role="admin",
    )
    regular_user = User(
        username="obnoxioustroll69",
        password="Please don't set passwords like this",
        email="trolliesttroll@example.com",
        first_name="Chad",
        last_name="Bowswick",
        bio="I leave hurtful comments on coding tutorials I find on the internet.",
        avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
    )
    admin_user = create_new_user(admin_user, session)
    regular_user = create_new_user(regular_user, session)
    LOGGER.success(f"Created 2 users: {admin_user} & {regular_user}")
    return admin_user, regular_user


def create_new_user(user: User, session: Session) -> User:
    """
    Create a new user if username isn't already taken.

    :param user: New user record to create.
    :type user: User
    :param session: SQLAlchemy database session.
    :type session: Session
    :return: Optional[User]
    """
    try:
        user_query = session.query(User).filter(User.username == user.username).first()
        if user_query is None:
            session.add(user)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created user: {user}")
        LOGGER.warning(f"User already exists in database: {user}")
        return user
    except IntegrityError as e:
        LOGGER.error(e.orig)


def create_post(session: Session) -> Post:
    """
    Create a post authored by `admin_user`.

    :param session: SQLAlchemy database session.
    :type session: Session

    :returns: Post
    """
    try:
        admin_user = session.query(User).filter(User.username == "toddthebod").first()
        post = Post(
            author_id=admin_user.id,
            slug="fake-post-slug",
            title="Fake Post Title",
            summary="A fake post to have some fake comments.",
            feature_image="https://hackersandslackers-cdn.storage.googleapis.com/2021/01/logo-smaller@2x.png",
            body="Cheese slices monterey jack cauliflower cheese dolcelatte cheese and wine fromage frais rubber cheese gouda. Rubber cheese cheese and wine cheeseburger cheesy grin paneer paneer taleggio caerphilly. Edam mozzarella.",
        )
        session.add(admin_user)  # Add the user
        session.commit()  # Commit the change
        LOGGER.success(f"Created post {post} published by user {admin_user}")
        return post
    except IntegrityError as e:
        LOGGER.error(e.orig)


def create_comment(session: Session) -> Comment:
    """
    Create a comment posted by `regular_user` on `admin_user`'s post.

    :param session: SQLAlchemy database session.
    :type session: Session

    :returns: Comment
    """
    try:
        regular_user = (
            session.query(User).filter(User.username == "obnoxioustroll69").first()
        )
        post = session.query(Post).filter(Post.id == 1).first()
        comment = Comment(
            user_id=regular_user.id,
            post_id=post.id,
            body="This post about SQLAlchemy is awful. You didn't even bother to explain how to install Python, which is where I (and so many others) got stuck. Plus, your code doesn't even work!! I cloned your code and it keeps giving me `environment variable` errors... WTF are environment variables?!!?!?",
            upvotes=2,
        )
        session.add(comment)  # Add the Comment
        session.commit()  # Commit the change
        LOGGER.success(f"Created comment {comment} posted by user {regular_user}")
        return comment
    except IntegrityError as e:
        LOGGER.error(e.orig)
