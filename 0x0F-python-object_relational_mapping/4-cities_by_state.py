#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    c = database.cursor()
    c.execute("SELECT cities.id, cities.name, states.name "
              "FROM cities "
              "JOIN states ON cities.state_id = states.id "
              "ORDER BY cities.id ASC ")
    for states in c.fetchall():
        print(states)
