#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument \
and lists all cities of the state using the database hbtn_0e_4_usa.

Usage:
    ./5-filter_cities.py <mysql username> <mysql password> \
<database name> <state name>
"""

import MySQLdb
import sys

if len(sys.argv) != 5:
    print("Usage: ./5-filter_cities.py <mysql username> <mysql \
password> <database name> <state name>")
else:
    # TODO: QUERY THE DATABASE.
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities as c \
            INNER JOIN states as s \
                ON c.state_id = s.id \
            ORDER BY c.id")  # TODO: QUERY
    query_rows = cur.fetchall()
    print(", ".join([row[2] for row in query_rows if row[4] == sys.argv[4]]))
    # for row in query_rows:
    #   if row[4] == sys.argv[4]:
    #        print(row)
    cur.close()
    conn.close()
