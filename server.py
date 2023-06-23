from flask import Flask, render_template, jsonify, request, Response
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


if __name__ == "__main__":
    app.run()