"""Execute raw SQL queries against an SQLAlchemy engine."""
from typing import List, Optional
import json

from sqlalchemy import text
from sqlalchemy.engine.base import Engine
from sqlalchemy.exc import SQLAlchemyError

from logger import LOGGER


def fetch_job_listings(engine: Engine) -> Optional[List[dict]]:
    """
    Select rows from database and parse as list of dicts.

    :param Engine engine: Database engine to handle raw SQL queries.

    :return: Optional[List[dict]]
    """
    try:
        LOGGER.info("Fetching job listings...")
        with engine.begin() as conn:
            result = conn.execute(
                text(
                    "SELECT job_id, agency, business_title, \
                    salary_range_from, salary_range_to \
                    FROM nyc_jobs ORDER BY RAND() LIMIT 5;"
                ),
            )
            results = result.fetchall()
            results_dict = [row._asdict() for row in results]
            LOGGER.info(f"Selected {result.rowcount} rows: {json.dumps(results_dict, indent=2)}")
            return results_dict
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError while fetching records: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching records: {e}")


def update_job_listing(engine: Engine) -> Optional[List[dict]]:
    """
    Update row in database with problematic characters escaped.

    :param Engine engine: Database engine to handle raw SQL queries.

    :return: Optional[List[dict]]
    """
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text(
                    "UPDATE nyc_jobs SET business_title = 'Senior QA Scapegoat 🏆', \
                    job_category = 'Information? <>!#%%Technology!%%#^&%* & Telecom' \
                    WHERE job_id = 229837;"
                )
            )
            LOGGER.success(f"Updated {result.rowcount} row: {result}")
            return result
    except SQLAlchemyError as e:
        LOGGER.error(f"SQLAlchemyError while updating records: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while updating records: {e}")
