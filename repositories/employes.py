from database import Database
from os import getenv


def append_to_database(table: str, login: str, password: str, funds: int):
    db = Database(getenv('DB'))
    return db.insert_table(table, None, login, password, funds)


def fetch_list(town: str):
    db = Database(getenv('DB'))
    return db.fetch_table('employes', town=town)


def delete_table(table: str):
    db = Database(getenv('DB'))
    return db.delete_table(table)


def fetch_all(table: str):
    db = Database(getenv('DB'))
    return db.fetch_all(table)


def check_funds():
    db = Database(getenv('DB'))
    return db.check_funds()
