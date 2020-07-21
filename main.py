import time

from service.sqlite_service import SQLiteService
from service.files_service import FileService
from service.file_reader_service import FileReaderService
from service.database_service import DatabaseService

# Time analysis
start_time = time.time()

# Create table
sqlite_connection, cursor = SQLiteService.open_sqlite()
DatabaseService.create_all_tables(cursor)


# Insert aujourdhui file in table
file = open(FileService.get_aujourdhui_file_path(), 'r')

number_of_duplicates = 0

lines = file.readlines()[1:]
for line in lines:
    try:
        DatabaseService.insert_line_in_db(
            sqlite_connection=sqlite_connection,
            cursor=cursor,
            line=line,
            database_name="professionals"
        )
    except Exception as e:
        professional_id = FileReaderService.get_professional_id(line)
        error_record = DatabaseService.get_professional_by_id(
            professional_id=professional_id,
            cursor=cursor
        )
        code_mode_exercice_1 = FileReaderService.get_code_mode_exercice(line)
        code_mode_exercice_2 = error_record[17]
        if code_mode_exercice_2 != code_mode_exercice_1:
            if code_mode_exercice_1 == "L" or code_mode_exercice_2 == "L":
                try:
                    DatabaseService.insert_line_in_db(
                        sqlite_connection=sqlite_connection,
                        cursor=cursor,
                        line=line,
                        database_name="new_liberals"
                    )
                except Exception as e:
                    pass
        number_of_duplicates += 1
        if number_of_duplicates%10 == 0:
            print("<----- Number of dupes: {} ------>".format(number_of_duplicates))


# Delete table for next execution
# todo remove this at the end of the project
# DatabaseService.delete_all_tables(cursor)
SQLiteService.close_sqlite(sqlite_connection, cursor)

# Time analysis
print("--- %s seconds ---" % (time.time() - start_time))
