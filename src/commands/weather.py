import click
from src.service import weather


class Context:
    def __init__(self, location):
        self.location = location
        self.weather = weather.Weather()


@click.group()
@click.option("-l", "--location", type=str, help="Weather at this location")
@click.pass_context
def cli(ctx, location):
    """Weather info"""
    ctx.obj = Context(location)


@cli.command()
@click.pass_context
def current(ctx):
    click.echo(ctx.obj.location)


@cli.command()
@click.pass_context
def forecast(ctx):
    pass
