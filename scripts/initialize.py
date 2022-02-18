from utils import config, deployment

ASTETH_IMPL_ADDRESS = "0xbd233D4ffdAA9B7d1d3E6b18CCcb8D091142893a"
STABLE_DEBT_STETH_IMPL_ADDRESS = "0x8180949ac41EF18e844ff8dafE604a195d86Aea9"
VARIABLE_DEBT_STETH_IMPL_ADDRESS = "0xDe2c414b671d2DB93617D1592f0490c13674de24"


def main():
    deployer = config.get_deployer_account(config.get_is_live())
    print("Deployer:", deployer)
    print("AStETH implementation address:", ASTETH_IMPL_ADDRESS)
    print("StableDebtStETH implementation address:", STABLE_DEBT_STETH_IMPL_ADDRESS)
    print("VariableDebtStETH implementation address:", VARIABLE_DEBT_STETH_IMPL_ADDRESS)

    sys.stdout.write("Proceed? [y/n]: ")
    if not config.prompt_bool():
        print("Aborting")
        return

    tx_params = {"from": deployer, "max_fee": "300 gwei", "priority_fee": "3 gwei"}

    initialize_asteth_impl(tx_params)
    initialize_stable_debt_steth_impl(tx_params)
    initialize_variable_debt_steth_impl(tx_params)


def initialize_asteth_impl(tx_params):
    asteth = deployment.AStETH.at(ASTETH_IMPL_ADDRESS)
    asteth.initialize(asteth.decimals(), asteth.name(), asteth.symbol(), tx_params)
    return asteth


def initialize_stable_debt_steth_impl(tx_params):
    stable_debt_steth = deployment.StableDebtStETH.at(STABLE_DEBT_STETH_IMPL_ADDRESS)
    stable_debt_steth.initialize(
        stable_debt_steth.decimals(),
        stable_debt_steth.name(),
        stable_debt_steth.symbol(),
        tx_params,
    )
    return stable_debt_steth


def initialize_variable_debt_steth_impl(tx_params):
    variable_debt_steth = deployment.VariableDebtStETH.at(
        VARIABLE_DEBT_STETH_IMPL_ADDRESS
    )
    variable_debt_steth.initialize(
        variable_debt_steth.decimals(),
        variable_debt_steth.name(),
        variable_debt_steth.symbol(),
        tx_params,
    )
    return variable_debt_steth
