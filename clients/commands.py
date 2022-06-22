from multiprocessing.connection import Client
import click
from clients.services import ClientsService
from clients.models import Client

@click.group
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option("-n", "--name",
            type = str,
            prompt=True,
            help="The client name")
@click.option("-c", "--company",
            type = str,
            prompt=True,
            help="The client company")
@click.option("-e", "--email",
            type = str,
            prompt=True,
            help="The client email")
@click.option("-p", "--position",
            type = str,
            prompt=True,
            help="The client position")
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientsService(ctx.obj["Clients_table"])

    client_service.create_client(client)
    

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
