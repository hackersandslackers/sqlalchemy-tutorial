"""Declare models and relationships."""
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import engine

Base = declarative_base()


class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    bio = Column(Text)
    avatar_url = Column(Text)
    role = Column(String(255))
    last_seen = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<User id={self.id}, username={self.username}, email={self.email}>"


class Comment(Base):
    """User-generated comment on a blog post."""

    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"), index=True)
    body = Column(Text)
    upvotes = Column(Integer, default=1)
    removed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user = relationship("User", backref="comment")

    def __repr__(self):
        return f"<Comment id={self.id}, post_id={self.post_id}, user_id={self.user_id}, upvotes={self.upvotes}, created_at={self.created_at}>"


class Post(Base):
    """Blog post/article."""

    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    slug = Column(String(255), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    summary = Column(String(400))
    feature_image = Column(String(300))
    body = Column(Text)
    status = Column(String(255), nullable=False, default="unpublished")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    # Relationships
    author = relationship("User", backref="posts")
    comments = relationship("Comment", backref="post")

    def __repr__(self):
        return f"<Post id={self.id}, slug={self.slug}, title={self.title}, body={self.body}>"


Base.metadata.create_all(engine)
