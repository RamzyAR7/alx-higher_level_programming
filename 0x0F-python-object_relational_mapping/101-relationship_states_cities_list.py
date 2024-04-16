#!/usr/bin/python3
"""
get data from database (CRD OP)
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    data = session.query(State).order_by(State.id)
    for value in data:
        print(f'{value.id}: {value.name}')
        for city in value.cities:
            print(f'\t{city.id}: {city.name}')
