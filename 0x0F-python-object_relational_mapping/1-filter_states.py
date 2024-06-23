#!/usr/bin/python3
import MySQLdb
from sys import argv


"""A script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states WHERE"
                "name LIKE BINARY 'N%' ORDER BY states.id")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
