#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.

Usage:
    ./100-relationship_states_cities.py <mysql username> <mysql password> \
<database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./100-relationship_states_cities.py <mysql username> <mysql \
password> <database name>")
    else:
        MySQL_USERNAME = sys.argv[1]
        MySQL_PASSWD = sys.argv[2]
        DB_NAME = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(MySQL_USERNAME, MySQL_PASSWD, DB_NAME), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(
                City(name="San Francisco",
                     state=State(name="California")))
        session.commit()
