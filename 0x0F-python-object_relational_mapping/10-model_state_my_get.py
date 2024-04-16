#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    name = sys.argv[4]

    obj = session.query(State).filter(State.name == name).first()
    if not obj:
        print("Not found")
    else:
        print(obj.id)
