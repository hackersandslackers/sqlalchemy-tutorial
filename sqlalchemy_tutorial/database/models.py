"""Declare models and relationships."""
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from sqlalchemy_tutorial.database import db

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
    last_seen = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<User %r>" % self.username


class Player(Base):
    """Individual player belonging to a team."""

    __tablename__ = "player"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    team_id = Column(Integer, ForeignKey("team.id"), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    position = Column(String(100), nullable=False)
    injured = Column(Boolean)
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Relationships
    team = relationship("Team")

    def __repr__(self):
        return "<Player {}>".format(self.id)


class Team(Base):
    """Team consisting of many players."""

    __tablename__ = "team"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    abbreviation = Column(String(255), nullable=False)
    logo = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<Team {}>".format(self.id)


def create_tables():
    return Base.metadata.create_all(db)
