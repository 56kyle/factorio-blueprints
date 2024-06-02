"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Factorio Blueprints."""


if __name__ == "__main__":
    main(prog_name="factorio-blueprints")  # pragma: no cover
