#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa

Usage:
    ./14-model_city_fetch_by_state.py <mysql username> <mysql password> \
<database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('./14-model_city_fetch_by_state.py <mysql username> <mysql \
password> <database name>')
    else:
        USERNAME = sys.argv[1]
        PASSWD = sys.argv[2]
        DB_NAME = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(USERNAME, PASSWD, DB_NAME), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        for city, state in session.query(City, State)\
            .filter(City.state_id == State.id)\
                .order_by(City.id):
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
