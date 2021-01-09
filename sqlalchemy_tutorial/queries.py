"""Executing raw SQL queries against an SQLAlchemy engine."""
from typing import List, Optional

from sqlalchemy import engine, text


def fetch_job_listings(db: engine) -> Optional[List[dict]]:
    """Select rows from database and parse as list of dicts."""
    results = db.execute(
        "SELECT job_id, agency, business_title, \
        salary_range_from, salary_range_to \
        FROM nyc_jobs ORDER BY RAND();"
    )
    print(f"Selected {results.rowcount} rows.")
    rows = [dict(row) for row in results.fetchall()]
    return rows


def update_job_listing(db: engine) -> Optional[List[dict]]:
    """Update row in database with problematic characters escaped."""
    result = db.execute(
        text(
            "UPDATE nyc_jobs SET business_title = 'Senior QA Scapegoat 🏆', \
            job_category = 'Information? <>!#%%Technology!%%#^&%* & Telecom' \
            WHERE job_id = 229837;"
        )
    )
    return result.rowcount
