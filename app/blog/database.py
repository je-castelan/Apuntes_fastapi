"""
More detail on https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALQUEMY = "sqlite:///./blog.db"

engine = create_engine(
    SQLALQUEMY,
    connect_args={"check_same_thread": False}
    ) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()