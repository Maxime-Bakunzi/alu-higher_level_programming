#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa

Usage:
    ./12-model_state_update_id_2.py <mysql username> <mysql password> \
<database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('./12-model_state_upadate_id_2.py <mysql username> <mysql \
password> <database name>')
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        update_State = session.query(State).filter_by(id=2).first()
        update_State.name = "New Mexico"
        session.commit()
