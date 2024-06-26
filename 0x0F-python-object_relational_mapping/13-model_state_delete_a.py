#!/usr/bin/python3
"""A script that deletes all State objects with a name containing the letter
    a from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    # Create the engine and session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all State objects with a name containing the letter 'a'
    session.query(State).filter(State.name.like('%a%')) \
        .delete(synchronize_session=False)

    # Commit the changes and close the session
    session.commit()
    session.close()
