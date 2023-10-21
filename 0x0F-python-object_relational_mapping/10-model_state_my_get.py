#!/usr/bin/python3
""" printing the State object with the name passed as argument from the database
hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    match = sys.argv[4]
    state = session.query(State).filter_by(name=match).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
