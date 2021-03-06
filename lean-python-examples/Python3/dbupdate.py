#!/usr/bin/env python3
#
#  Copyright (c) 2014 Paul Gerrard
#  This program is free software.
#  license: GNU General Public License version 3
#
#  This code is an example from `Lean Python`: http://leanpy.com/
#
import sqlite3
import sys
#
#   arguments from command line
#
if len(sys.argv) <3:
    print('Usage: python3 dbupdate.py 1 Chinese')
    exit()
#
#   use: python dbupdate.py   1  Chinese
#
db_filename = 'mydatabase.db'
inid = sys.argv[1]
innat = sys.argv[2]
#
#   execute update using command line arguments
#
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
query = "update person set nationality = :nat where id = :id"
cursor.execute(query, {'id':inid, 'nat':innat})
#
#   list the persons to see changes
#   
cursor.execute("select id, name, dob,nationality,gender from person")
for row in cursor.fetchall():
    id, name, dob,nationality,gender = row
    print("%3d %15s %12s %10s %6s" % (id, name, dob,nationality,gender))

