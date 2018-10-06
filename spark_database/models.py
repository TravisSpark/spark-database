"""
Hold Objects for SQL Tables
"""
import sqlalchemy as sa
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    Attributes for members of Phoenix Spark
    """
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, unique = True)
    phone = sa.Column(sa.String)
    unit = sa.Column(sa.String)
    section = sa.Column(sa.String)
    date_joined = sa.Column(sa.DateTime, default = sa.func.now())
    rfid = sa.Column(sa.String, unique=True)
