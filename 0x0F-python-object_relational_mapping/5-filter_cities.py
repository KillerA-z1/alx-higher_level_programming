#!/usr/bin/python3
"""A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query to select cities
    query = "SELECT cities.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id"
    cur.execute(query, (argv[4],))

    # Fetch all the rows and extract the city names
    cities = [row[0] for row in cur.fetchall()]

    # Print the cities separated by commas
    print(", ".join(cities))
    # Close the cursor and the database connection
    cur.close()
    db.close()
