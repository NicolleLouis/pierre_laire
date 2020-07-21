import time

from service.sqlite_service import SQLiteService
from service.files_service import FileService
from service.file_reader_service import FileReaderService

from db_query import sqlite_create_table_query, sqlite_print_table, sqlite_drop_table

# Time analysis
start_time = time.time()

# Create table
sqliteConnection, cursor = SQLiteService.open_sqlite()
try:
    cursor.execute(sqlite_create_table_query)
except Exception as e:
    print("<----- Error: {} ------>".format(e))
    pass

# Insert aujourdhui file in table
file = open(FileService.get_aujourdhui_file_path(), 'r')
lines = file.readlines()[1:]
for line in lines:
    try:
        FileReaderService.insert_line_in_db(
            sqliteConnection=sqliteConnection,
            cursor=cursor,
            line=line
        )
    except Exception as e:
        print(line)
        print(e)

# Look at table
cursor.execute(sqlite_print_table)

# Delete table for next execution
# todo remove this a the end of the project
# cursor.execute(sqlite_drop_table)
SQLiteService.close_sqlite(sqliteConnection, cursor)

# Time analysis
print("--- %s seconds ---" % (time.time() - start_time))
