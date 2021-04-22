import os
import click


class ComplexCLI(click.MultiCommand):
    """Initiate complex CLI."""

    def list_commands(self, ctx):
        """List available commands for this CLI."""
        commands = []
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), "commands")):
            if filename.endswith(".py") and not filename.startswith("__"):
                commands.append(filename.replace(".py", ""))
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        """Import command to use in the CLI."""
        try:
            mod = __import__(f"src.commands.{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """Welcome to JARVIS"""
    pass
