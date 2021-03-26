#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database...
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
    louisiana = State(name='Louisiana', id=6)
    session.add(louisiana)
    session.commit()
    print("{}".format(louisiana.id))
    session.close()
