from db_query import sqlite_get_line_by_id, sqlite_create_table_query, \
    sqlite_insert_line, sqlite_drop_table, sqlite_delete_by_id

from service.file_reader_service import FileReaderService


class DatabaseService:
    @staticmethod
    def get_professional_by_id(professional_id, cursor):
        cursor.execute(sqlite_get_line_by_id.format(professional_id))
        record = cursor.fetchone()
        return record

    @staticmethod
    def create_db(cursor, database_name):
        try:
            cursor.execute(sqlite_create_table_query.format(database_name=database_name))
        except Exception as e:
            print("<----- Error: {} ------>".format(e))
            pass

    @staticmethod
    def delete_instance_by_professional_id_in_aujourdhui_db(
            cursor,
            professional_id
    ):
        sqlite_delete = sqlite_delete_by_id.format(professional_id)
        cursor.execute(sqlite_delete)

    @staticmethod
    def insert_line_in_db(
            sqlite_connection,
            cursor,
            line,
            database_name
    ):
        sqlite_insert = sqlite_insert_line.format(
            database_name=database_name,
            *FileReaderService.read_line(line)
        )
        cursor.execute(sqlite_insert)
        sqlite_connection.commit()

    @staticmethod
    def delete_all_tables(cursor):
        try:
            cursor.execute(sqlite_drop_table.format(database_name="professionals"))
        except Exception as e:
            pass
        try:
            cursor.execute(sqlite_drop_table.format(database_name="new_liberals"))
        except Exception as e:
            pass
        try:
            cursor.execute(sqlite_drop_table.format(database_name="liberals_hier_and_aujourdhui"))
        except Exception as e:
            pass

    @staticmethod
    def create_all_tables(cursor):
        DatabaseService.create_db(
            cursor=cursor,
            database_name="professionals"
        )
        DatabaseService.create_db(
            cursor=cursor,
            database_name="new_liberals"
        )
        DatabaseService.create_db(
            cursor=cursor,
            database_name="liberals_hier_and_aujourdhui"
        )

