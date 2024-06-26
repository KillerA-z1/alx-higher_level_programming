#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    [print(state) for state in cur.fetchall()]
    # Close the cursor and the database connection
    cur.close()
    db.close()
