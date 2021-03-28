from database import session
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User

from .joins import get_all_comments, get_all_posts
from .objects import create_comment_objects, create_post_object, create_user_objects
from .orm import create_comment, create_user, create_post


def create_relationships():
    """
    Use SQLAlchemy's ORM to create objects with relationships.

    :return: None
    """
    # Create admin & regular user
    admin_user, regular_user = create_user_objects()
    admin_user = create_user(session, admin_user)
    regular_user = create_user(session, regular_user)

    # Create post object and add to database
    post_1, post_2 = create_post_object(admin_user)
    post_1 = create_post(session, post_1)
    post_2 = create_post(session, post_2)

    # Create comments on the same post
    (
        comment_1,
        comment_2,
        comment_3,
        comment_4,
        comment_5,
    ) = create_comment_objects(regular_user, admin_user, post_1, post_2)
    create_comment(session, comment_1)
    create_comment(session, comment_2)
    create_comment(session, comment_3)
    create_comment(session, comment_4)
    create_comment(session, comment_5)

    # One-to-many JOIN for a given user
    get_all_posts(session, admin_user)

    # Show posts with comments:
    get_all_comments(session)
