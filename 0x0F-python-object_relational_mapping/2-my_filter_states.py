#!/usr/bin/python3
"""
Takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where
name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(
        host="localhost", user=argv[1],
        password=argv[2], database=argv[3], port=3306)
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE"
        " '{:s}' ORDER BY id ASC".format(argv[4])
    )
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
