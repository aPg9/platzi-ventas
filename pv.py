import click 
from clients import commands as clients_commands

CLIENTS_TABLE = ".clients.csv"         
@click.group
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj["clients_table"] = CLIENTS_TABLE

cli.add_command(clients_commands.all)     #-----> Del modulo clients se importa commands como clients_commands y dentro del modulo se usa la variable all q es un alias de clients
