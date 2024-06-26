#!/usr/bin/python3
"""A script that changes the name of a State object from the
    database hbtn_0e_6_usa"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update the name of the State object with id 2
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"

    # Commit the changes and close the session
    session.commit()
    session.close()
