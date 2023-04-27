#!/usr/bin/python3
"""
script that takes in an argument \
and displays all values in the states table of hbtn_0e_0_usa \
where name matches the argument.

Usage: ./3-my_safe_filter_states.py <mysql username> \
<mysql password <database name> <argument>
"""
import MySQLdb
import sys


# Test the no. of commandline arguements passed
if len(sys.argv) == 5:
    # Connect to MySQL
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = conn.cursor()
    # Grab all values in the states table.
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

else:
    print("Usage: ./3-my_safe_filter_states.py \
<mysql username> <mysql password <database name>")
