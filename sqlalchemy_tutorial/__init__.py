"""Run source code for each tutorial found on HackersAndSlackers."""
from database import db, session

from .logger import LOGGER
from .part1_connections import fetch_job_listings, update_job_listing
from .part2_orm_models import orm_create_user, orm_delete_user


def init_script():
    """Run all scripts."""

    # Part 1: Executing SELECT and UPDATE queries with an SQLAlchemy engine
    LOGGER.info("Part 1: Executing queries against an SQLAlchemy engine.")
    fetch_job_listings(db)
    update_job_listing(db)

    # Part 2: Implementing an ORM
    LOGGER.info("Part 2: Create and delete records from a data model.")
    orm_create_user(session)
    orm_delete_user(session)