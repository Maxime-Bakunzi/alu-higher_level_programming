#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.i

Usage:
    ./102-relationship_cities_states_list.py <mysql username> \
<mysql password> <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./102-relationship_cities_states_list.py <mysql username> \
<mysql password> <database name>")
    else:
        MySQL_USERNAME = sys.argv[1]
        MySQL_PASSWD = sys.argv[2]
        DB_NAME = sys.argv[3]

        engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}\
".format(MySQL_USERNAME, MySQL_PASSWD, DB_NAME), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        for city in session.query(City).order_by(City.id):
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
