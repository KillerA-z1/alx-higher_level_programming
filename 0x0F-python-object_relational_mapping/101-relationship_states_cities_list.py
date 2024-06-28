#!/usr/bin/python3
"""
This script lists all State objects and their corresponding City objects.

The script takes three command-line arguments: username, password, and dbname.
It connects to a MySQL database using the provided credentials and retrieves
all State objects from the database. For each State object, it prints the state
ID and name. It then retrieves all City objects associated with the state and
prints their IDs and names as well.

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City


if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{dbname}',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
