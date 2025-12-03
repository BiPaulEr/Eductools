import argparse
from eductools.math_tools import (
    add,
    subtract,
)  # Ajustez l'import selon votre structure de package
import click
from eductools.math_tools import add, subtract  # Adjust the import as needed

@click.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
@click.option(
    "--operation",
    help="L'opération à effectuer: add ou subtract",
    default="add",
    show_default=True,
    type=click.Choice(["add", "subtract"], case_sensitive=False)
)
def calcul_cli(a, b, operation):
    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    else:
        raise click.BadParameter("Opération non supportée.")
    
    print(f"Résultat: {result}")

if __name__ == "__main__":
    calcul_cli()

