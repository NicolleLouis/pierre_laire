from db_query import sqlite_insert_line


class FileReaderService:
    @staticmethod
    def read_line(line):
        values = line.split("|")
        values = list(map(lambda value: "\"{}\"".format(value) if value != "" else "NULL", values))
        return values

    @staticmethod
    def insert_line_in_db(sqliteConnection, cursor, line):
        sqlite_insert = sqlite_insert_line.format(*FileReaderService.read_line(line))
        cursor.execute(sqlite_insert)
        sqliteConnection.commit()
