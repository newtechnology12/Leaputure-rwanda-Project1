from email.policy import default
from pydoc import cli
import click

@click.group()
def createDB():
    print("create data base")

@click.command()
def deleteDB():
    print ("DELETE DATA BASE")

@click.command()
@click.option('--count', default=1, help = 'number of greating')
@click.argument('name')
def hello(count, name):
    print(f'hello {name}!')

cli.add_command(createDB)
cli.add_command(deleteDB)
cli.add_command(hello)

if __name__ == '__main__':
    cli()