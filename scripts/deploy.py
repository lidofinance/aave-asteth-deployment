import sys
from brownie import ZERO_ADDRESS, Wei, web3
from utils import deployment, config, lido, aave, constants


def main():
    deployer = config.get_deployer_account(config.get_is_live())
    lending_pool_address = aave.lending_pool_address_provider().getLendingPool()
    print("Deployer:", deployer)
    print("StETH:", lido.STETH_ADDRESS)
    print("AAVE Treasury:", aave.TREASURY_ADDRESS)
    print("AAVE Lending Pool:", lending_pool_address)
    print_strategy_config()
    validate_contract_hashes()

    sys.stdout.write("Proceed? [y/n]: ")
    if not config.prompt_bool():
        print("Aborting")
        return

    tx_params = {"from": deployer, "max_fee": "100 gwei", "priority_fee": "2 gwei"}

    deploy_implementation_and_strategy(
        lending_pool_address, tx_params, publish_source=False
    )


def deploy_implementation_and_strategy(
    lending_pool_address, tx_params, publish_source=False
):
    asteth_impl = deployment.deploy_asteth_impl(
        lending_pool_address,
        lido.STETH_ADDRESS,
        aave.TREASURY_ADDRESS,
        tx_params,
        publish_source,
    )
    stable_debt_steth_impl = deployment.deploy_stable_debt_steth_impl(
        lending_pool_address, lido.STETH_ADDRESS, tx_params, publish_source
    )
    variable_debt_steth_impl = deployment.deploy_variable_debt_steth_impl(
        lending_pool_address, lido.STETH_ADDRESS, tx_params, publish_source
    )
    steth_interest_rate_strategy = deployment.deploy_steth_intereset_rate_strategy(
        tx_params, publish_source
    )
    return (
        asteth_impl,
        stable_debt_steth_impl,
        variable_debt_steth_impl,
        steth_interest_rate_strategy,
    )


def compute_sources_hashes(contract):
    sources = contract.get_verification_info()["standard_json_input"]["sources"]
    result = {}
    for source_file_name, source in sources.items():
        code_hash = web3.keccak(text=source["content"])
        result[source_file_name] = code_hash.hex()
    return result


def validate_contract_hashes():
    contract_names = [
        "AStETH",
        "StableDebtStETH",
        "VariableDebtStETH",
        "DefaultReserveInterestRateStrategy",
    ]
    print("Validate contract hashes:")
    for contract_name in contract_names:
        actual_contract_hash = compute_sources_hashes(
            getattr(deployment, contract_name)
        )[f"{contract_name}.sol"]
        expected_contract_hash = constants.VALID_CONTRACT_HASHES[contract_name]
        print(f"  {contract_name}:")
        print(f"    expected hash: {expected_contract_hash}")
        print(f"    actual hash  : {actual_contract_hash}")
        if expected_contract_hash != actual_contract_hash:
            print("    Contract hashes are not equal! Exiting...")
            sys.exit()
        assert actual_contract_hash == expected_contract_hash

    print("All contract hashes are valid. Good to go!")
    print()


def format_ray_with_percents(value):
    return format_percents(value, constants.ONE_RAY)


def format_percents(value, percentage_factor=10 ** 4):
    return f"{value} ({100 * value / percentage_factor :3.2f}%)"


def print_strategy_config():
    strategy = constants.STRATEGY_STETH
    print("Strategy Config:")
    print(
        f'  Optimal Utilization Rate: {format_ray_with_percents(strategy["optimalUtilizationRate"])}'
    )
    print(
        f'  Base Variable Borrow Rate: {format_ray_with_percents(strategy["baseVariableBorrowRate"])}'
    )
    print(
        f'  Variable Rate Slope 1: {format_ray_with_percents(strategy["variableRateSlope1"])}'
    )
    print(
        f'  Variable Rate Slope 2: {format_ray_with_percents(strategy["variableRateSlope2"])}'
    )
    print(
        f'  Stable Rate Slope 1: {format_ray_with_percents(strategy["stableRateSlope1"])}'
    )
    print(
        f'  Stable Rate Slope 2: {format_ray_with_percents(strategy["stableRateSlope2"])}'
    )
    print(
        f'  Base LTV As Collateral: {format_percents(strategy["baseLTVAsCollateral"])}'
    )
    print(
        f'  Liquidation Threshold: {format_percents(strategy["liquidationThreshold"])}'
    )
    print(f'  Liquidation Bonus: {format_percents(strategy["liquidationBonus"])}')
    print(f'  Borrowing Enabled: {strategy["borrowingEnabled"]}')
    print(f'  Stable Borrow Rate Enabled: {strategy["stableBorrowRateEnabled"]}')
    print(f'  Reserve Decimals: {strategy["reserveDecimals"]}')
    print(f'  Reserve Factor: {strategy["reserveFactor"]}')
    print()
