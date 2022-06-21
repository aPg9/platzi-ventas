import click

@click.group
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """List all clietns"""
    pass


@clients.command()
@click.pass_context
def updated(ctx, client_uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass


all = clients
