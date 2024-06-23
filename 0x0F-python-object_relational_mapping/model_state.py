#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
"""Class definition of a State and an instance Base = declarative_base()"""


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":

    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine("mysql://localhost:3306")

    # Create the tables in the database
    Base.metadata.create_all(engine)
