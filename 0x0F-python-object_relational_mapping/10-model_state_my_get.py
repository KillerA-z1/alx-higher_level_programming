#!/usr/bin/python3
"""A script that prints the State object with the name passed as an argument
    from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    # Create the engine and session
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects and check if the name matches the argument
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the result or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
