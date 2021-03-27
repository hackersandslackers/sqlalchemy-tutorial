"""Initialize objects from data models to generate in Database."""
from typing import Tuple

from sqlalchemy_tutorial.part3_relationships.models import Comment, Post, User


def create_user_objects() -> Tuple[User, User]:
    """
    Set up an admin user to own a `Post`, and regular user to add comments.

    :return: Tuple[User, User]
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
    return admin_user, regular_user


def create_post_object(admin_user: User) -> Post:
    """
    Set up post to add to database.

    :param admin_user: User to serve as post author.
    :type admin_user: User

    :return: Post
    """
    return Post(
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


def create_comment_objects(
    regular_user: User, post: Post
) -> Tuple[Comment, Comment, Comment]:
    """
    Set up 3 comments to be added to published post.

    :param regular_user: User to serve as comment author.
    :type regular_user: User
    :param post: Blog post to be created.
    :type post: Post

    :return: Tuple[Comment, Comment, Comment]
    """
    comment_1 = Comment(
        user_id=regular_user.id,
        post_id=post.id,
        body="This post about SQLAlchemy is awful. You didn't even bother to explain how to install Python, \
              which is where I (and so many others) got stuck. Plus, your code doesn't even work!! \
              I cloned your code and it keeps giving me `environment variable` errors... \
              WTF are environment variables?!!?!?",
        upvotes=2,
    )
    comment_2 = Comment(
        user_id=regular_user.id,
        post_id=post.id,
        body="By the way, you SUCK!!! I HATE you!!!! I have a project due tomorrow, how am I supposed to finish \
             if you won't do my job for me, you selfish prick?!?!",
        upvotes=5,
    )
    comment_3 = Comment(
        user_id=regular_user.id,
        post_id=post.id,
        body="YOU RUINED MY LIFE!!!!",
        upvotes=5,
    )
    return comment_1, comment_2, comment_3
