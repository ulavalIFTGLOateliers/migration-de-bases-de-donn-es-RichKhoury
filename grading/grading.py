from database import Database


class Grader():
    def __init__(self):
        self.database = Database()


class MySQLGrader(Grader):
    def __init__(self):
        super().__init__()

    def migration_1(self):
        self.database.migrate1()