#!/usr/bin/python3
"""A script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.But this time,
write one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
    [print(state) for state in cur.fetchall()]
    # Close the cursor and the database connection
    cur.close()
    db.close()
