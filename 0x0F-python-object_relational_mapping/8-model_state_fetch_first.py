#!/usr/bin/python3
"""   script that prints the first State object from the database...
    ...hbtn_0e_6_usa """


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           ("root", "root", argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).filter_by(id='1'):
        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")
    session.close()
#  could not clear not table so did not test if printing nothing works
