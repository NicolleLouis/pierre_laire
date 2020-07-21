import sqlite3


class SQLiteService:
    @staticmethod
    def open_sqlite():
        sqliteConnection = sqlite3.connect('sqlite.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        return sqliteConnection, cursor

    @staticmethod
    def close_sqlite(sqliteConnection, cursor):
        cursor.close()
        sqliteConnection.close()
        print("The SQLite connection is closed")
