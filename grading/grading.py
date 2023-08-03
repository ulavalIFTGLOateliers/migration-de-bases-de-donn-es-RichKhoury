from database import Database
from collections import OrderedDict
from grading_utils import failable
from sql_utils import run_select


class Grader:
    def __init__(self):
        """
            Cette interface sert à corriger les soumissions des étudiants.

            Il est possible d'ajouter autant de tests que désiré, ainsi que modifier les tests existants
            Tous les tests doivent être ajoutés au dictionnaire self.grading_template, dans la section correspondante parmis:
                - up
                - after_migration_1
                - after_rollback_1
                - after_migration_2
                - after_rollback_2

            ATTENTION: les sections migration_1, rollback_1, migration_2 et rollback_2 ne peuvent PAS être modifiées, sauf leur nombre de points respectif.

            Chaque entrée de ce dictionnaire doit être de la forme:

                    "[nom du test]": {
                        "callable": callable,    # fonction de test retournant un booléen
                        "points": int,           # nombre de points
                        "passed": Bool           # statut de réussite du test
                    }
        """

        self.grading_template = OrderedDict({
            "up": {
                "connexion": {
                    "callable": self._up,
                    "points": 1,
                    "passed": False
                }
            },
            "migration_1": {
                "migration 1": {
                    "callable": self._migration_1,
                    "points": 1,
                    "passed": False
                }
            },
            "after_migration_1": {
                "schema des tables": {
                    "callable": self._check_schema_after_migration_1,
                    "points": 1,
                    "passed": False
                },
                "contenu de album": {
                    "callable": self._check_album_tuples_after_migration_1,
                    "points": 1,
                    "passed": False
                },
                "contenu de band": {
                    "callable": self._check_band_tuples_after_migration_1,
                    "points": 1,
                    "passed": False
                },
                "contenu de label": {
                    "callable": self._check_label_tuples_after_migration_1,
                    "points": 1,
                    "passed": False
                },
                "contenu de musician": {
                    "callable": self._check_musician_tuples_after_migration_1,
                    "points": 1,
                    "passed": False
                }
            },
            "rollback_1": {
                "rollback 1": {
                    "callable": self._rollback_1,
                    "points": 1,
                    "passed": False
                }
            },
            "after_rollback_1": {

            },
            "migration_2": {
                "migration 2": {
                    "callable": self._migration_2,
                    "points": 1,
                    "passed": False
                }
            },
            "after_migration_2": {

            },
            "rollback_2": {
                "rollback 2": {
                    "callable": self._rollback_2,
                    "points": 1,
                    "passed": False
                }
            },
            "after_rollback_2": {

            }
        })

    def run(self):
        self._run_section_tests("up")
        if not self.grading_template["up"]["connexion"]["passed"]:
            return

        self._run_section_tests("migration_1")
        if not self.grading_template["migration_1"]["migration 1"]["passed"]:
            return

        self._run_section_tests("after_migration_1")

    def generate_report(self):
        pass

    def _run_section_tests(self, section):
        for test_attributes in self.grading_template[section].values():
            test_attributes["passed"] = test_attributes["callable"]()

    @failable
    def _up(self):
        self.database = Database()
        self.cursor = self.database.get_cursor()
        self.database.get_connection().ping(reconnect=False)
        self.database.up()
        return True

    @failable
    def _migration_1(self):
        self.database.push_migration()
        return True

    @failable
    def _check_schema_after_migration_1(self):
        target_table_names = ["album", "label", "band", "musician"]
        actual_table_names = self.database.get_table_names()
        if sorted(target_table_names) != sorted(actual_table_names):
            return False

        target_album_column_names = ["albumName", "singerName", "year", "labelName"]
        actual_album_column_names = self.database.get_table_column_names("album")
        if sorted(target_album_column_names) != sorted(actual_album_column_names):
            return False

        target_band_column_names = ["bandName", "creation", "genre"]
        actual_band_column_names = self.database.get_table_column_names("band")
        if sorted(target_band_column_names) != sorted(actual_band_column_names):
            return False

        target_label_column_names = ["labelName", "creation", "genre"]
        actual_label_column_names = self.database.get_table_column_names("label")
        if sorted(target_label_column_names) != sorted(actual_label_column_names):
            return False

        target_musician_column_names = ["musicianName", "firstName", "lastName", "age", "role", "bandName"]
        actual_musician_column_names = self.database.get_table_column_names("musician")
        if sorted(target_musician_column_names) != sorted(actual_musician_column_names):
            return False

        return True

    @failable
    def _check_album_tuples_after_migration_1(self):
        target_tuples = [("Concertos", "Luna", 2009, "Four Seasons"),
                         ("Second Mystery", "Mysterio", 2021, "World Music"),
                         ("World of Mysteries", "Mysterio", 2019, "Dark Matter")]
        actual_tuples = run_select(self.cursor, "SELECT * FROM album;")
        return sorted(target_tuples) == sorted(actual_tuples)

    @failable
    def _check_band_tuples_after_migration_1(self):
        target_tuples = [("Crazy Duo", 2015, "rock"),
                         ("Mysterio", 2019, "pop"),
                         ("Luna", 2009, "classical")]
        actual_tuples = run_select(self.cursor, "SELECT * FROM band;")
        return sorted(target_tuples) == sorted(actual_tuples)

    @failable
    def _check_label_tuples_after_migration_1(self):
        target_tuples = [("Dark Matter", 2015, "rock"),
                         ("Four Seasons", 1999, "classical"),
                         ("World Music", 2002, "pop")]
        actual_tuples = run_select(self.cursor, "SELECT * FROM label;")
        return sorted(target_tuples) == sorted(actual_tuples)

    @failable
    def _check_musician_tuples_after_migration_1(self):
        target_tuples = [("Alina", "Darcy", "Boles", 32, "vocals", "Crazy Duo"),
                         ("Luna", "Emily", "Seibold", 31, "piano", "Luna"),
                         ("Mysterio", "Jessie", "Chancey", 23, "guitar", "Mysterio"),
                         ("Rainbow", "Sarah", "Derrick", 47, "percussion", "Crazy Duo")]
        actual_tuples = run_select(self.cursor, "SELECT * FROM musician;")
        return sorted(target_tuples) == sorted(actual_tuples)

    def _rollback_1(self):
        pass

    def _migration_2(self):
        pass

    def _rollback_2(self):
        pass

    def test(self):
        return self.grading_template




# class MySQLGrader(Grader):
#     def __init__(self):
#         super().__init__()
#
#     def migration_1(self):
#         self.database.migrate1()




if __name__ == '__main__':
    grader = Grader()

    grader.run()

    print(grader.test())