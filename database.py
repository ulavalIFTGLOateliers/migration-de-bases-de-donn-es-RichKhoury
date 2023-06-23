import pymysql
from decouple import config

from sql_utils import run_sql_file


class Database:
    def __init__(self):
        self.cursor = self.open_sql_connection()

        self.database_name = config("DATABASE")

    @staticmethod
    def open_sql_connection():
        """
        Opens an pymysql connection to a database using environment variables.

        You must complete the code in order to get the missing values from environment variables defined in your .env file

        :return: pymysql.cursor
        """

        host = config("HOST")
        port = config("PORT", default=3306, cast=int)
        database = config("DATABASE")
        user = config("USER")
        password = config("PASSWORD")

        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=database,
            autocommit=True
        )

        cursor = connection.cursor()

        return cursor

    def up(self):
        run_sql_file(self.cursor, "up.sql")

    def migrate(self):
        run_sql_file(self.cursor, "migrate.sql")

    def rollback(self):
        run_sql_file(self.cursor, "rollback.sql")

    def get_table_names(self):
        req = f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_type = 'BASE TABLE' AND table_schema = '{self.database_name}';"
        self.cursor.execute(req)

        res = [x[0] for x in self.cursor.fetchall()]

        return res

    def get_table_column_names(self, table):
        req = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}' AND TABLE_SCHEMA = '{self.database_name}' ORDER BY ORDINAL_POSITION;"
        self.cursor.execute(req)

        res = [x[0] for x in self.cursor.fetchall()]

        return res

    def get_table_data(self, table):
        req = f"SELECT * FROM {table};"
        self.cursor.execute(req)

        return list(self.cursor.fetchall())


if __name__ == '__main__':
    d = Database()
    tables = d.get_table_names()

    for table in tables:
        print("table")
        print(d.get_table_column_names(table))
        print(d.get_table_data(table))