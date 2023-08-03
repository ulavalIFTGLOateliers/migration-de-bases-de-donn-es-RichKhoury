import pymysql
from decouple import config

from sql_utils import run_sql_file


class Database:
    def __init__(self):
        """
            Complétez les lignes 13 à 17 afin de récupérer les valeurs des variables d'environnement situées dans votre fichier .env
        """

        self.host = config("HOST")
        self.port = config("PORT", default=3306, cast=int)
        self.database = config("DATABASE")
        self.user = config("USER")
        self.password = config("PASSWORD")

        self._open_sql_connection()

        self.migration_counter = 0

    def _open_sql_connection(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database,
            autocommit=True
        )

        self.cursor = self.connection.cursor()

    def push_migration(self):
        migration_to_push = self.migration_counter + 1
        migration_file = f"db_scripts/migrate_{migration_to_push}.sql"

        run_sql_file(self.cursor, migration_file)
        self.migration_counter += 1

    def rollback(self):
        if self.migration_counter < 1:
            raise ValueError("There are no rollbacks in the rollback stack.")

        rollback_file = f"db_scripts/rollback_{self.migration_counter}.sql"

        run_sql_file(self.cursor, rollback_file)
        self.migration_counter -= 1

    def up(self):
        self.drop()
        run_sql_file(self.cursor, "db_scripts/up.sql")

    def drop(self):
        run_sql_file(self.cursor, "db_scripts/drop.sql")
        self.migration_counter = 0

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

    def get_cursor(self):
        return self.cursor

    def get_connection(self):
        return self.connection