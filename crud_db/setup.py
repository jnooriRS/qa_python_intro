#Exercise - Using my code as reference, create your own basic CRD app 
# Creates a table, Create records, read all records, read one record(by id, name..), deletes one record
# Stretch goal(s):
# Use input to get inputs
# Add update queries
# Add a second table (relational) (TOUGH GOAL)
# Multiple files for resilience

import sqlite3

def create_connection(dbName):
    # Returning a connection object when creating a DB
    return sqlite3.connect(dbName)

# Table is created as oart of set up
# Cursor to execute command and create table in string format

def create_table(cursor, query):
    cursor.execute(query): # query will be table
    return True
