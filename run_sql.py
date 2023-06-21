import argparse

from database.database import Database
from database.sql_utils import run_sql_file


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="inputfile", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    input_file = args.input
    cursor = Database.open_sql_connection()

    run_sql_file(cursor, input_file)


if __name__ == '__main__':
    main()
