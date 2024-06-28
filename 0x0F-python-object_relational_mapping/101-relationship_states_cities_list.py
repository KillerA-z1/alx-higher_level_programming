#!/usr/bin/python3
"""
This script lists all State objects and their corresponding City objects.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Extracts username,password, and database name from command line arguments
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Creates engine instance
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{dbname}',
        pool_pre_ping=True
    )

    # Creates all tables by issuing CREATE TABLE commands to the database
    Base.metadata.create_all(engine)

    # Creates a sessionmaker factory bound to this engine
    Session = sessionmaker(bind=engine)
    # Creates a new Session instance
    session = Session()

    # Queries all State objects, ordered by their id
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        # Iterates through each City object related to the current State object
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
