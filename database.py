import pymysql
from decouple import config

from sql_utils import run_sql_file


class Database:
    def __init__(self):
        """
            Complétez les lignes 14 à 18 afin de récupérer les valeurs des variables d'environnement situées dans votre fichier .env
        """

        self.host = config("HOST")
        self.port = config("PORT", default=3306, cast=int)
        self.database = config("DATABASE")
        self.user = config("USER")
        self.password = config("PASSWORD")

        self.cursor = self.open_sql_connection()

    def open_sql_connection(self):
        connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database,
            autocommit=True
        )

        cursor = connection.cursor()

        return cursor

    def up(self):
        self.drop()
        run_sql_file(self.cursor, "db_scripts/up.sql")

    def migrate(self):
        run_sql_file(self.cursor, "db_scripts/migrate.sql")

    def rollback(self):
        run_sql_file(self.cursor, "db_scripts/rollback.sql")

    def drop(self):
        run_sql_file(self.cursor, "db_scripts/drop.sql")

    def get_table_names(self):
        req = f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_type = 'BASE TABLE' AND table_schema = '{self.database}';"
        self.cursor.execute(req)

        res = [x[0] for x in self.cursor.fetchall()]

        return res

    def get_table_column_names(self, table):
        req = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}' AND TABLE_SCHEMA = '{self.database}' ORDER BY ORDINAL_POSITION;"
        self.cursor.execute(req)

        res = [x[0] for x in self.cursor.fetchall()]

        return res

    def get_table_data(self, table):
        req = f"SELECT * FROM {table};"
        self.cursor.execute(req)

        return list(self.cursor.fetchall())
