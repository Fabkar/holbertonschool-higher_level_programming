#!/usr/bin/python3
"""that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    c = database.cursor()
    c.execute("SELECT * "
              "FROM states "
              "WHERE name =%s ORDER BY states.id ASC ", (sys.argv[4],))
    for states in c.fetchall():
        print(states)
