"""Run source code for each tutorial found on HackersAndSlackers."""
from config import CLEANUP_DATA
from logger import LOGGER

from .cleanup import cleanup_data
from .part1_connections import execute_queries
from .part2_orm import create_and_delete_users
from .part3_relationships import create_relationships


def init_script():
    """Run all scripts."""

    # Part 1: Executing SELECT and UPDATE queries with an SQLAlchemy engine
    LOGGER.info("----------------------------------------------------")
    LOGGER.info("Part 1: Executing queries against an SQLAlchemy engine.")
    execute_queries()

    # Part 2: Implementing an ORM
    LOGGER.info("----------------------------------------------------")
    LOGGER.info("Part 2: Create and delete records from a data model.")
    create_and_delete_users()

    # Part 3: ORM relationships
    LOGGER.info("----------------------------------------------------")
    LOGGER.info("Part 3: Utilize relationships to execute JOINs.")
    create_relationships()

    # OPTIONAL: Reset table data after each run
    if CLEANUP_DATA:
        LOGGER.info("----------------------------------------------------")
        LOGGER.info("Purging all created data...")
        cleanup_data()
