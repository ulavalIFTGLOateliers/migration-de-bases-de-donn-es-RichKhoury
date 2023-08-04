import os


def parse_sql(filename):
    """
    Parses a .sql file and returns statements in a list of strings

    :param filename: the .sql file to be parsed
    :return: list of statements
    """

    current_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(current_dir, filename)


    data = open(abs_file_path, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for lineno, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip())
            stmt = ''
        else:
            stmts.append(line.strip())
    return stmts


def run_sql_file(cursor, filename):
    """
    Executes each statement iteratively from a .sql file.
    The target database is the one specified by your environment variables.

    :param cursor: an open pymysql.cursor
    :param filename: the .sql file to execute
    """
    sql_statements = parse_sql(filename)

    for statement in sql_statements:
        cursor.execute(statement)
