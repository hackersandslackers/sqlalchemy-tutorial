"""Script entry point."""
from sqlalchemy_tutorial.models import create_tables


def init_script():
    result = create_tables()
    print(result)

