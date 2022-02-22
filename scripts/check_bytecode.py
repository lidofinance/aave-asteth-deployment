from brownie import web3, network, accounts
from scripts.deploy import deploy_implementation_and_strategy
from utils import aave, config

deployed_contracts = {
    "AStETH": "0xbd233D4ffdAA9B7d1d3E6b18CCcb8D091142893a",
    "StableDebtStETH": "0x8180949ac41EF18e844ff8dafE604a195d86Aea9",
    "VariableDebtStETH": "0xDe2c414b671d2DB93617D1592f0490c13674de24",
    "DefaultReserveInterestRateStrategy": "0xff04ed5f7a6C3a0F1e5Ea20617F8C6f513D5A77c",
}


def main():
    if config.get_is_live():
        print(
            "The current network is not supported.",
            "Please, rerun the script in the mainnet-fork network.",
        )
        exit()

    print("Loading contracts bytecode from mainnet...")
    deployed_contracts_bytecode = load_contracts_bytecode(deployed_contracts)

    print("Deploying contracts to mainnet fork...")
    lending_pool_address = aave.lending_pool_address_provider().getLendingPool()
    (
        asteth_impl,
        stable_debt_steth_impl,
        variable_debt_steth_impl,
        steth_interest_rate_strategy,
    ) = deploy_implementation_and_strategy(lending_pool_address, {"from": accounts[0]})

    print("Loading bytecode of newly deployed contracts from mainnet fork...")
    newly_deployed_contracts_bytecode = load_contracts_bytecode(
        {
            "AStETH": asteth_impl.address,
            "StableDebtStETH": stable_debt_steth_impl.address,
            "VariableDebtStETH": variable_debt_steth_impl.address,
            "DefaultReserveInterestRateStrategy": steth_interest_rate_strategy.address,
        }
    )

    compare_bytecodes(deployed_contracts_bytecode, newly_deployed_contracts_bytecode)


def load_contracts_bytecode(contracts):
    res = {}
    for contract_name, contract_address in contracts.items():
        print(f"Loading bytecode for contract {contract_name} ({contract_address})...")
        res[contract_name] = web3.eth.getCode(contract_address).hex()
        print(
            f"Bytecode successfully loaded:", res[contract_name], sep="\n", end="\n\n"
        )
    return res


def compare_bytecodes(actual, expected):
    print("Validating that bytecode of contracts matches...")
    is_all_matches = True
    for contract_name in actual.keys():
        if compare_bytecode_except_ipfs_hash(
            actual[contract_name], expected[contract_name]
        ):
            print(f"  [OK] {contract_name}")
        else:
            print(f"  [Error!] {contract_name} bytecodes don't match!")
            is_all_matches = False

    if is_all_matches:
        print("All contracts bytecode matches!", end="\n\n")
    else:
        print("The bytecode of some contracts doesn't match!", end="\n\n")


def compare_bytecode_except_ipfs_hash(actual, expected):
    actual_except_ipfs_hash = trunc_ipfs_hash(actual)
    expected_except_ipfs_hash = trunc_ipfs_hash(expected)
    return actual_except_ipfs_hash == expected_except_ipfs_hash


def trunc_ipfs_hash(bytecode):
    """
    Truncates IPFS hash from metadata section in bytecode.
    See https://docs.soliditylang.org/en/v0.6.12/metadata.html#encoding-of-the-metadata-hash-in-the-bytecode
    """
    ipfs_metadata_opcodes = "a264697066735822"  # 0xa2 0x64 'i' 'p' 'f' 's' 0x58 0x22 sequence of bytes between ipfs hash
    ipfs_hash_length = 68  # 34 bytes
    ipfs_metdata_opcodes_index = bytecode.index(ipfs_metadata_opcodes)
    return (
        bytecode[: ipfs_metdata_opcodes_index + len(ipfs_metadata_opcodes)]
        + bytecode[
            ipfs_metdata_opcodes_index + len(ipfs_metadata_opcodes) + ipfs_hash_length :
        ]
    )
