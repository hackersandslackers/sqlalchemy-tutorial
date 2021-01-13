"""Execute raw SQL queries against an SQLAlchemy engine."""
from typing import List, Optional

from sqlalchemy import engine, text

from sqlalchemy_tutorial.logger import LOGGER


def fetch_job_listings(db: engine) -> Optional[List[dict]]:
    """
    Select rows from database and parse as list of dicts.

    :param db: Engine object representing a SQL database.
    :type db: engine

    :returns: Optional[List[dict]]
    """
    results = db.execute(
        "SELECT job_id, agency, business_title, \
        salary_range_from, salary_range_to \
        FROM nyc_jobs ORDER BY RAND();"
    )
    rows = [dict(row) for row in results.fetchall()]
    LOGGER.info(
        f"Selected {results.rowcount} rows: \
        {rows}"
    )
    return rows


def update_job_listing(db: engine) -> Optional[List[dict]]:
    """
    Update row in database with problematic characters escaped.

    :param db: Engine object representing a SQL database.
    :type db: engine

    :returns: Optional[List[dict]]
    """
    result = db.execute(
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
