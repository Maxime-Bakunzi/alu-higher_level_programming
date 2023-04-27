#!/usr/bin/python3
"""
script that lists all states from database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
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
    cur.execute("SELECT * from states")  # Grab all the states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
else:
    print("Usage: ./0-select_states.py <mysql username>\
 <mysql password> <database name>")
