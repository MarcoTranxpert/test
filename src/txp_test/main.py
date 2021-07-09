import click


@click.group()
def cli_entrypoint():
    pass


@click.command()
def hello():
    click.echo("Hello world")

cli_entrypoint.add_command(hello)

if __name__ == "__main__":
    cli_entrypoint()