from dotenv import load_dotenv
import sqlite3
from sqlite3 import Error

load_dotenv()


class Database:
    def __init__(self, database_name: str):
        try:
            self.connect = sqlite3.connect(database_name)
            self.cursor = self.connect.cursor()
        except Error:
            print(f'Error {Error} ')

    def __del__(self):
        self.connect.close()

    def create_table(self, table: str):
        self.cursor.execute(
            f'CREATE TABLE {table}('
            f'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
            f'login varchar,'
            f'password text,'
            f'funds integer)')
        self.connect.commit()

    def insert_table(self, table: str, *args):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in args])})", args)
        self.connect.commit()

    def fetch_table(self, table: str, **kwargs):
        values = kwargs.values()
        query = self.cursor.execute(
            # "SELECT * FROM employes WHERE town=?" town
            f"SELECT * FROM {table} WHERE {'and'.join([f'{kwarg}=?' for kwarg in kwargs])}", list(values))
        return query.fetchall()

    def fetch_all(self, table: str):
        query = self.cursor.execute(f"SELECT * FROM {table}")
        return query.fetchall()

    def delete_table(self, table: str):
        self.cursor.execute(f'DROP TABLE {table}')
        self.connect.commit()

    def check_account(self, username: str, password: str):
        self.cursor.execute("SELECT * FROM users WHERE login=? AND password = ?", (username, password))
        result = self.cursor.fetchone()
        self.connect.commit()
        return result

    def check_funds(self):
        query = self.cursor.execute("SELECT login,funds FROM users")
        return query.fetchall()




