import json
import os

import click
import requests
from dotenv import load_dotenv


@click.command()
@click.option('--mac_address', help='Please Enter MAC ADDRESS')
def get_campeny_name(mac_address):
    """ using mac_address getting the CAMPENY NAME"""
    data = requests.get(
        f"https://api.macaddress.io/v1?apiKey={os.getenv('API_KEY')}&output=json&search={mac_address}"
    )
    results = json.loads(data.content)
    click.echo(results['vendorDetails']['companyName'])


if __name__ == '__main__':
    load_dotenv()
    get_campeny_name()
