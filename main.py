from sqlite_service import SQLiteService
from db_query import sqlite_create_table_query, sqlite_print_table, sqlite_drop_table

sqliteConnection, cursor = SQLiteService.open_sqlite()
# Create table
cursor.execute(sqlite_create_table_query)

#Insert aujourdhui file in table

# Look at table
cursor.execute(sqlite_print_table)

# Delete table for next execution
cursor.execute(sqlite_drop_table)
SQLiteService.close_sqlite(sqliteConnection, cursor)
