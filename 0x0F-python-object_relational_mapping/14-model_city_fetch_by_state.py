#!/usr/bin/python3
"""
get data from database (CRD OP)
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    data = session.query(State.name, City.id, City.name)\
        .filter(State.id == City.state_id)
    for value in data:
        print(f'{value[0]}: ({value[1]}) {value[2]}')
