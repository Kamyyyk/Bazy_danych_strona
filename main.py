from commands import cli, create_command, add_command,fetch_command,delete_command,login_command, fetch_all_command, \
    check_funds_command

from dotenv import load_dotenv

load_dotenv()

cli.add_command(create_command)
cli.add_command(add_command)
cli.add_command(create_command)
cli.add_command(fetch_command)
cli.add_command(delete_command)
cli.add_command(login_command)
cli.add_command(fetch_all_command)
cli.add_command(check_funds_command)


if __name__ == '__main__':
    cli()

# if argv[1] == 'create' and len(argv) == 3:
#     print("Creating table...")
#     table_name = argv[2]
#     db = Database(getenv('DB'))
#     db.create_table(table_name)

# if argv[1] == 'add' and len(argv) == 6:
#     name = argv[2]
#     surname = argv[3]
#     age = argv[4]
#     town = argv[5]
#     db = Database(getenv('DB'))
#     db.insert_table(None, name, surname, age, town)
#     print(f'{name} {surname} has been added to database')

# if argv[1] == 'list' and len(argv) == 3:
#     print(f'Lista imion o pasujących danych')
#     town = argv[2]
#     db = Database(getenv('DB'))
#     names = db.fetch_table('employes', town=town)
#
#     for link in names:
#         print(link)
#
# if argv[1] == 'delete' and len(argv) == 3:
#     table_name = argv[2]
#     db = Database(getenv('DB'))
#     db.delete_table(table_name)
#     print(f'Deleting table: {table_name}')
