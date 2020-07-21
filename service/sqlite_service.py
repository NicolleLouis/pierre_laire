import sqlite3


class SQLiteService:
    @staticmethod
    def open_sqlite():
        sqliteConnection = sqlite3.connect('sqlite.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        return sqliteConnection, cursor

    @staticmethod
    def close_sqlite(sqlite_connection, cursor):
        cursor.close()
        sqlite_connection.close()
        print("The SQLite connection is closed")
