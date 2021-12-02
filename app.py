from flask import Flask, jsonify
from commands import cli, add_command, fetch_command, fetch_all_command, login_command, \
    check_funds_command

app = Flask(__name__)


@app.route("/append/", methods=['POST'])
def append_to_list(table: str, login: str, password: str, funds: int):
    print("Dodaje elementy do tabeli")


@app.route("/test")
def fetch_funds():
    funds = check_funds_command()
    for i in funds:
        print(i)


@app.route("/list/<town>")
def fetch_list(town: str):
    users = fetch_command(town)
    return jsonify(users)


@app.route("/list/<table>")
def fetch_list_all(table: str):
    users = fetch_all_command(table)
    return users


@app.route("/delete/<table>")
def delete_table(table: str):
    return f"{table}"


@app.route("/login/<login>")
def login_to_account(login: str, password: str):
    log = login_command(login, password)
    return log
