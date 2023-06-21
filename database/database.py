import pymysql
from decouple import config

from database.sql_utils import run_sql_file


class Database:
    def __init__(self):
        self.cursor = self.open_sql_connection()

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
