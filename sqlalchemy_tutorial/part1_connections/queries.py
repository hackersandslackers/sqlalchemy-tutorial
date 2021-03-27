"""Execute raw SQL queries against an SQLAlchemy engine."""
from typing import List, Optional

from sqlalchemy import text
from sqlalchemy.engine.base import Engine

from logger import LOGGER


def fetch_job_listings(engine: Engine) -> Optional[List[dict]]:
    """
    Select rows from database and parse as list of dicts.

    :param engine: Database engine to handle raw SQL queries.
    :type engine: engine

    :return: Optional[List[dict]]
    """
    result = engine.execute(
        text(
            "SELECT job_id, agency, business_title, \
            salary_range_from, salary_range_to \
            FROM nyc_jobs ORDER BY RAND();"
        )
    )
    rows = [dict(row) for row in result.fetchall()]
    LOGGER.info(f"Selected {result.rowcount} rows: {rows}")
    return rows


def update_job_listing(engine: Engine) -> Optional[List[dict]]:
    """
    Update row in database with problematic characters escaped.

    :param engine: Engine object representing a SQL database.
    :type engine: engine

    :return: Optional[List[dict]]
    """
    result = engine.execute(
        text(
            "UPDATE nyc_jobs SET business_title = 'Senior QA Scapegoat 🏆', \
            job_category = 'Information? <>!#%%Technology!%%#^&%* & Telecom' \
            WHERE job_id = 229837;"
        )
    )
    LOGGER.info(
        f"Selected {result.rowcount} row: \
        {result}"
    )
    return result.rowcount
