from database import session
from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User

from .joins import get_posts
from .orm import create_comment, create_post, create_users


def create_relationships():
    """
    Use SQLAlchemy's ORM to create objects with relationships.

    :return: None
    """
    admin_user = User(
        username="toddthebod",
        password="Password123lmao",
        email="todd@example.com",
        first_name="Todd",
        last_name="Birchard",
        bio="I write tutorials on the internet.",
        avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
        role="admin",
    )
    regular_user = User(
        username="obnoxioustroll69",
        password="Password123rofl",
        email="trolliesttroll@example.com",
        first_name="Chad",
        last_name="Bowswick",
        bio="I leave hurtful comments on coding tutorials I find on the internet.",
        avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
    )
    post = Post(
        author_id=admin_user.id,
        slug="fake-post-slug",
        title="Fake Post Title",
        status="published",
        summary="A fake post to have some fake comments.",
        feature_image="https://hackersandslackers-cdn.storage.googleapis.com/2021/01/logo-smaller@2x.png",
        body="Cheese slices monterey jack cauliflower cheese dolcelatte cheese and wine fromage frais rubber \
                cheese gouda. Rubber cheese cheese and wine cheeseburger cheesy grin paneer paneer taleggio caerphilly. \
                Edam mozzarella.",
    )
    admin_user, regular_user = create_users(session, admin_user, regular_user)
    new_post = create_post(session, post, admin_user)
    create_comment(session, regular_user, new_post)
