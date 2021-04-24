import os
import click


class ComplexCLI(click.MultiCommand):
    """Initiate complex CLI."""

    def list_commands(self, ctx):
        """List available commands for this CLI."""
        commands = []
        commands_folder = os.path.join(os.path.dirname(__file__), "commands")
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace("cmd_", "").replace(".py", ""))
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        """Import command to use in the CLI."""
        try:
            mod = __import__(f"src.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """Welcome to JARVIS"""
    pass
