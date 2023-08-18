from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
                "mysql+mysqldb://scott:tiger@localhost/test",
                isolation_level="READ UNCOMMITTED"
            )


def get_db_connection():
    db = engine.raw_connection()
    try:
        yield db
    finally:
        db.close()
