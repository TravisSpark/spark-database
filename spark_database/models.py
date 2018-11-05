"""
Hold Objects for SQL Tables and Manage Database Session
"""
from contextlib import contextmanager
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import sys
sys.path.insert(0, './')
import settings


ENGINE = sa.create_engine(URL(**settings.DATABASE))
SESSION = sessionmaker(bind=ENGINE)

@contextmanager
def session_scope():
    """ Control the SQL Database Session  """
    session = SESSION()
    try:
        yield session
        session.commit()
        print("sql command succeeded")
    except:
        session.rollback()
        print("sql command failed")
    finally:
        session.close()

Base = declarative_base()

class User(Base):
    """
    Attributes for members of Phoenix Spark
    """
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, unique=True)
    phone = sa.Column(sa.String)
    unit = sa.Column(sa.String)
    section = sa.Column(sa.String)
    date_joined = sa.Column(sa.DateTime, default=sa.func.now())
    rfid = sa.Column(sa.String, unique=True)
