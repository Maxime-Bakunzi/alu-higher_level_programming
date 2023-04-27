#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if len(sys.argv) == 4:
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
            FROM cities as c \
            INNER JOIN states as s \
            ON `c`.`state_id` = s.id \
            ORDER BY c.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

else:
    print("Usage ./4-cities_by_state.py <mysql username> \
<mysql password> <database name>")
