import click
from db_provisioner import DBProvisioner

@click.command()
@click.option('--flavor', prompt='Tipo', help='O tipo do banco de dados (pequeno, médio, grande).')
@click.option('--storage', prompt='Tamanho do armazenamento', help='O tamanho do armazenamento em GB.')
def create_db(flavor, storage):
    response = DBProvisioner.provision(flavor, storage)
    print(response['message'])

if __name__ == '__main__':
    create_db()