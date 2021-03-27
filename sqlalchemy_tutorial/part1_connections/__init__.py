from database import engine

from .queries import fetch_job_listings, update_job_listing


def execute_queries():
    """
    Fetch and update records using raw SQL queries.

    :return: None
    """
    fetch_job_listings(engine)
    update_job_listing(engine)
