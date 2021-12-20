#!/usr/bin/python3
"""
a script that lists name of states
from a database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", user=argv[1],
        password=argv[2], database=argv[3], port=3306)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
