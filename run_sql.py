import argparse
import pymysql
from decouple import config


def open_sql_connection():
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


def parse_sql(filename):
    data = open(filename, 'r').readlines()
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


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="inputfile", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    input_file = args.input

    sql_statements = parse_sql(input_file)

    cursor = open_sql_connection()

    for statement in sql_statements:
        cursor.execute(statement)


if __name__ == '__main__':
    main()