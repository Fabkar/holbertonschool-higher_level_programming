#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from
    the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    c = database.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
    for states in c.fetchall():
        if states[1][0] == "N":
            print(states)
