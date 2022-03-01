# Click is library for creating beautiful command line interfaces in easy way.
import click
from cs50 import get_int
@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):

    for i in range(10):
        click.echo(f"Hello, {name},!")



if __name__ == '__main__':
    hello()
#flake8 is great library toolkit for checking your code base against coding style, programming errors(like library mported but unused and undefined name)
#run it use python3 -m flake8 clickLibrary.py
 #McCabe automatically detects over-complex code basing on cyclomatic complexity
 #run it use python3 -m mccabe clickLibrary.py
# pyflakes is a simple program that checks Python source code for errors.
