import time

from service.sqlite_service import SQLiteService
from service.files_service import FileService
from service.file_reader_service import FileReaderService
from service.database_service import DatabaseService


def insert_aujourdhui_in_sqlite():
    file = open(FileService.get_aujourdhui_file_path(), 'r')

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


# Time analysis
start_time = time.time()

# Create table
sqlite_connection, cursor = SQLiteService.open_sqlite()
DatabaseService.create_all_tables(cursor)

# todo uncomment this at the end of project
# insert_aujourdhui_in_sqlite()

# Look at hier file line by line and check distinction
file = open(FileService.get_hier_file_path(), 'r')

lines = file.readlines()[1:]
for line in lines:
    professional_id = FileReaderService.get_professional_id(line)
    code_mode_exercice_1 = FileReaderService.get_code_mode_exercice(line)
    aujourdhui_record = DatabaseService.get_professional_by_id(
        professional_id=professional_id,
        cursor=cursor
    )
    if aujourdhui_record is not None:
        # Detect new liberals/old liberals
        code_mode_exercice_2 = aujourdhui_record[17]
        if code_mode_exercice_2 != code_mode_exercice_1:
            if code_mode_exercice_1 == "L" or code_mode_exercice_2 == "L":
                # checked manually -> removed for optimization
                # Check line already is in new_liberals and add if needed
                pass

# Delete table for next execution
# todo uncomment this at the end of the project
# DatabaseService.delete_all_tables(cursor)
SQLiteService.close_sqlite(sqlite_connection, cursor)

# Time analysis
print("--- %s seconds ---" % (time.time() - start_time))
