import csv
import time

from service.sqlite_service import SQLiteService
from service.files_service import FileService
from service.file_reader_service import FileReaderService
from service.database_service import DatabaseService


def delete_duplicate_hier_aujourdhui(cursor):
    # Look at hier file line by line and check differences
    file = open(FileService.get_hier_file_path(), 'r', encoding="utf-8")

    new_liberals_hier = 0

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
                    new_liberals_hier += 1
                    if new_liberals_hier % 100 == 0:
                        print("<-- New liberals hier: {} -->".format(new_liberals_hier))
                    # Used to save the line with L instead of any line
                    if code_mode_exercice_2 == "L":
                        line = FileReaderService.convert_instance_to_line(aujourdhui_record)
                    try:
                        DatabaseService.insert_line_in_db(
                            sqlite_connection=sqlite_connection,
                            cursor=cursor,
                            line=line,
                            database_name="new_liberals"
                        )
                    except Exception as e:
                        pass
                    try:
                        DatabaseService.insert_line_in_db(
                            sqlite_connection=sqlite_connection,
                            cursor=cursor,
                            line=line,
                            database_name="liberals_hier_and_aujourdhui"
                        )
                    except Exception as e:
                        pass
            # Remove aujourdhui record since it's not new
            DatabaseService.delete_instance_by_professional_id_in_aujourdhui_db(
                cursor=cursor,
                professional_id=professional_id
            )
    sqlite_connection.commit()


def insert_aujourdhui_in_sqlite():
    file = open(FileService.get_aujourdhui_file_path(), 'r', encoding="utf-8")

    lines = file.readlines()[1:]
    number_of_lines_analysed = 0
    for line in lines:
        number_of_lines_analysed += 1
        if number_of_lines_analysed % 1000 == 0:
            print("<-- Lines analysed: {} -->".format(number_of_lines_analysed))
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
                if code_mode_exercice_1 == "L":
                    try:
                        DatabaseService.insert_line_in_db(
                            sqlite_connection=sqlite_connection,
                            cursor=cursor,
                            line=line,
                            database_name="new_liberals"
                        )
                    except Exception as e:
                        pass
                if code_mode_exercice_2 == "L":
                    record_as_line = FileReaderService.convert_instance_to_line(error_record)
                    try:
                        DatabaseService.insert_line_in_db(
                            sqlite_connection=sqlite_connection,
                            cursor=cursor,
                            line=record_as_line,
                            database_name="new_liberals"
                        )
                    except Exception as e:
                        # print("<-- Exception: {} -->".format(e))
                        print("Line in reverse order")
                        pass


def save_result_in_csv():
    cursor.execute("SELECT * FROM new_liberals")
    open("docs/new_liberals_2_ligne.csv", "w").close()
    with open("docs/new_liberals_2_ligne.csv", "w") as new_liberals_file:
        csv_writer = csv.writer(new_liberals_file, delimiter="|")
        csv_writer.writerows(cursor)
    cursor.execute("SELECT * FROM professionals")
    open("docs/new_professionals.csv", "w").close()
    with open("docs/new_professionals.csv", "w") as professionals_file:
        csv_writer = csv.writer(professionals_file, delimiter="|")
        csv_writer.writerows(cursor)
    cursor.execute("SELECT * FROM liberals_hier_and_aujourdhui")
    open("docs/liberals_hier_aujourdhui.csv", "w").close()
    with open("docs/liberals_hier_aujourdhui.csv", "w") as professionals_file:
        csv_writer = csv.writer(professionals_file, delimiter="|")
        csv_writer.writerows(cursor)


# Time analysis
start_time = time.time()

# Create table
sqlite_connection, cursor = SQLiteService.open_sqlite()
DatabaseService.create_all_tables(cursor)

insert_aujourdhui_in_sqlite()
print("## Today file saved in db -> Start of yesterday comparison ##")
delete_duplicate_hier_aujourdhui(cursor=cursor)

save_result_in_csv()

# Delete table for next execution
# DatabaseService.delete_all_tables(cursor)
SQLiteService.close_sqlite(sqlite_connection, cursor)

# Time analysis
print("--- %s seconds ---" % (time.time() - start_time))
