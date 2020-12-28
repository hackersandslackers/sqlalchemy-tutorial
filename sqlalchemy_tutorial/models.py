"""Declare models and relationships."""
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_tutorial.database import engine

Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("team_id", Integer, ForeignKey("sport.player.team_id")),
    Column("id", Integer, ForeignKey("sport.team.id")),
)


class Player(Base):
    """Individual player object."""

    __tablename__ = "player"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    team_id = Column(Integer, ForeignKey("sport.team.id"), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    position = Column(String(100), nullable=False)
    injured = Column(Boolean)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, server_default=text("NOW()"), nullable=False)

    # Relationships
    team = relationship("Team")

    def __repr__(self):
        return "<Person model {}>".format(self.id)


class Team(Base):
    """Sport team consisting of players."""

    __tablename__ = "team"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, server_default=text("NOW()"), nullable=False)

    def __repr__(self):
        return "<Team model {}>".format(self.id)


def create_tables():
    return Base.metadata.create_all(engine)

