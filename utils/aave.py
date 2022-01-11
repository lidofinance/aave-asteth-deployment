from brownie import interface

TREASURY_ADDRESS = "0x464c71f6c2f760dda6093dcb91c24c39e5d6e18c"
LENDING_POOL_ADDRESS_PROVIDER = "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5"


def lending_pool_address_provider(interface=interface):
    return interface.LendingPoolAddressProvider(LENDING_POOL_ADDRESS_PROVIDER)
