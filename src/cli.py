"""
Entry point for the jarvis CLI tool
"""
import click


@click.command()
def cli():
    """All commands starts here"""
    click.echo('Hello, World!')
