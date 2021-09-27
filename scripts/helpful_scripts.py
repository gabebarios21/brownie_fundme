from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")

    if len(MockV3Aggregator) <= 0:
        # we need to deploy the contract as usual.
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    # like this [-1] we take the latest one. latest deployed.
    print("mocks deployed!")
