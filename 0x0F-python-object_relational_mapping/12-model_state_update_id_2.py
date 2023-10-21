#!/usr/bin/python3
""" changing the name of a State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'
    session.commit()
