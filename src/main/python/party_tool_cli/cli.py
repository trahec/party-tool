"""
Command line client for your custom party!
"""

import os
import click

from party_handler import PartyHandler

@click.group()
def main():
    # tool description
    """
    party-tool <option> --help

    A command line tool, which helps you to party!

    """


@main.command()
@click.option('--name', required=True,
              help="Name of your party")
@click.option('--custom-party',
              help="path to directory which contains files for a custom party\
                    Default party '.' ")
def create(name, custom_party):
    print("Configuring party...")
    config = {}
    config['party_name'] = name
    config['custom_party_dir'] = custom_party

    party_handler = PartyHandler()
    try:
        party = party_handler.create_party(config)
        print("_____________\n")
        print party
        print("\n_____________")
    except Exception as e:
        print e
