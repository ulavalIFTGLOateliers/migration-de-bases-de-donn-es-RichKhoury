from flask import Flask, render_template, Response
from database import Database

app = Flask(__name__)

database = Database()


@app.route("/")
def index():
    table_names = database.get_table_names()

    tables = []
    for table_name in table_names:
        table_dict = {
            "name": table_name,
            "columns": database.get_table_column_names(table_name),
            "entries": database.get_table_data(table_name)
        }

        tables.append(table_dict)

    return render_template("index.html", tables=tables)


@app.route("/migrate", methods=["POST"])
def migrate():
    try:
        database.migrate()
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=406)


@app.route("/up", methods=["POST"])
def up():
    try:
        database.up()
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=406)


@app.route("/rollback", methods=["POST"])
def rollback():
    try:
        database.rollback()
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=406)


if __name__ == "__main__":
    app.run()