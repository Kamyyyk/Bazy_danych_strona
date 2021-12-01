from commands import cli, create_command, add_command,fetch_command,delete_command,login_command, fetch_all_command, \
    check_funds_command

from dotenv import load_dotenv

load_dotenv()

cli.add_command(create_command)
cli.add_command(add_command)
cli.add_command(fetch_all_command)
cli.add_command(check_funds_command)
cli.add_command(fetch_command)
cli.add_command(login_command)
cli.add_command(delete_command)


if __name__ == '__main__':
    cli()