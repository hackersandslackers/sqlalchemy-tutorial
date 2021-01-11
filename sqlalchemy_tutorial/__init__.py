"""Script entry point."""
import pprint

from sqlalchemy_tutorial.database.connect import db
from sqlalchemy_tutorial.database.models import create_tables
from sqlalchemy_tutorial.orm import orm_create_user
from sqlalchemy_tutorial.queries import fetch_job_listings, update_job_listing

# Print formatter
pp = pprint.PrettyPrinter(indent=4, width=300)


def init_script():
    """Demonstrate SELECT and UPDATE queries with SQLAlchemy."""
    create_tables()
    rows_selected = fetch_job_listings(db)
    pp.pprint(rows_selected)
    rows_updated = update_job_listing(db)
    print(rows_updated)
    user = orm_create_user()
    print(user)
