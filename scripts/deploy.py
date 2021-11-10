from brownie import Factory, accounts, network
import click


def main():
    click.echo(f"You are using the '{network.show_active()}' network")
    dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
    click.echo(f"You are using: 'dev' [{dev.address}]")

    dev.deploy(Factory, max_fee = "98 gwei", priority_fee="2 gwei", nonce=4,)
