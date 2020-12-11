#!/usr/bin/python3
# lists all states with a name starting with N (upper N) from
# the database hbtn_0e_0_usa.

import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    c = database.cursor()
    c.execute("SELECT * \
                FROM states \
                WHERE name = '{}' ORDER BY states.id ASC".format(sys.argv[4]))
    for states in c.fetchall():
        print(states)
