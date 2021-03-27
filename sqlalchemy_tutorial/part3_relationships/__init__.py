from database import session
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User

from .joins import list_all_comments
from .objects import create_comment_objects, create_post_object, create_user_objects
from .orm import create_comment, create_new_user, create_post


def create_relationships():
    """
    Use SQLAlchemy's ORM to create objects with relationships.

    :return: None
    """
    # Create admin & regular user
    admin_user, regular_user = create_user_objects()
    admin_user = create_new_user(session, admin_user)
    regular_user = create_new_user(session, regular_user)

    # Create post object and add to database
    post = create_post_object(admin_user)
    post = create_post(session, post, admin_user)

    # Create three comments on the same post
    (
        comment_1,
        comment_2,
        comment_3,
    ) = create_comment_objects(regular_user, post)
    create_comment(session, regular_user, comment_1)
    create_comment(session, regular_user, comment_2)
    create_comment(session, regular_user, comment_3)

    # Show post with comments:
    list_all_comments(session)
