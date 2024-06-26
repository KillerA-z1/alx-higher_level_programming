#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Execute the SQL query
    query = """SELECT id, name
         FROM states
         WHERE name='{}'
         ORDER BY id ASC""".format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
