from brownie import accounts, config, FundMe, network, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIROMENTS,
)


# brownie run scripts/deploy.py --network rinkeby

# if we are on a persisten network like rinkeby, use the assress. otherwise, deploy moks.
def deploy_fm():
    account = get_account()  # is the first one from ganache. Not ours. test!
    # pass the price feed address to our fundme contract.

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]  # ETH/USD rinkeby by chainlink.
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fm()
