import click
from database import Database
from os import getenv
from repositories.users import fetch_list, delete_table, fetch_all, check_funds, append_to_database


@click.group()
def cli():
    pass


@click.command(name='create')
@click.argument('table_name')
def create_command(table_name: str):
    print("Creating table...")
    db = Database(getenv('DB'))
    db.create_table(table_name)


@click.command(name='append')
@click.argument('table')
@click.argument('login')
@click.argument('password')
@click.argument('funds')
def add_command(table: str, login: str, password: str, funds: int):
    add = append_to_database(table, login,password,funds)
    print(f'{login} has been added to table {table}')
    return add


@click.command(name='list')
@click.argument('town')
def fetch_command(town: str):
    print(f'Lista użytkowników pochodzących z miasta {town}')

    for i in fetch_list(town):
        print(i)


@click.command(name='listall')
@click.argument('table')
def fetch_all_command(table: str):
    print(f"Wszysto z tabeli {table} :")
    fetch_everything = fetch_all(table)
    for users in fetch_everything:
        print(users)

@click.command(name='funds')
def check_funds_command():
    query = check_funds()
    return str(query)


@click.command(name='delete')
@click.argument('table_name')
def delete_command(table_name: str):
    delete_table(table_name)
    print(f'Table {table_name} has been deleted from database.')


@click.command(name='login')
@click.argument('user')
@click.argument('password')
def login_command(user: str, password: str):
    db = Database(getenv('DB'))
    log = db.check_account(user, password)
    if log:
        print("Logged!")
    else:
        print("Bad password or login!")
