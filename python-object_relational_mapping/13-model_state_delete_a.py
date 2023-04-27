#!/usr/bin/python3
"""
Script that deletes all State Objects with a name containing the letter a \
from the database hbtn_0e_6_usa

Usage:
    ./13-model_state_delete_a.py <mysql username> <mysql password> <database \
name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username> <mysql \
password> <database name>")
    else:
        MYSQL_USERNAME = sys.argv[1]
        MYSQL_PASSWORD = sys.argv[2]
        DATABASE_NAME = sys.argv[3]

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(MYSQL_USERNAME, MYSQL_PASSWORD, DATABASE_NAME), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        for state in session.query(State):
            if 'a' in state.name:
                session.delete(state)
        session.commit()
