#!/usr/bin/python3
"""  script that prints the State object with the name passed as argument...
    ...from the database hbtn_0e_6_usa """


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           ("root", "root", argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not Found")
    session.close()
