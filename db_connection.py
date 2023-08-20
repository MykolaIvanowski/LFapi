from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_URL = "mysql+pymysql://root:password@localhost/LFapi"
engine = create_engine(
                SQL_URL,
                isolation_level="READ UNCOMMITTED"
            )
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db_connection():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
