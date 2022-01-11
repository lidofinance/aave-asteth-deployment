from brownie import ZERO_ADDRESS
from utils import aave, constants, helpers
from utils.helpers import DependencyLoader


AAVE_DEPENDENCY_NAME = "lidofinance/aave-protocol-v2@1.0.2-rc.1"


AStETH = helpers.DependencyLoader.load(AAVE_DEPENDENCY_NAME, "AStETH")
VariableDebtStETH = helpers.DependencyLoader.load(
    AAVE_DEPENDENCY_NAME, "VariableDebtStETH"
)
StableDebtStETH = helpers.DependencyLoader.load(AAVE_DEPENDENCY_NAME, "StableDebtStETH")
DefaultReserveInterestRateStrategy = helpers.DependencyLoader().load(
    AAVE_DEPENDENCY_NAME, "DefaultReserveInterestRateStrategy"
)


def deploy_asteth_impl(lending_pool, steth, treasury, tx_params, publish_source=False):
    return AStETH.deploy(
        lending_pool,  # lending pool,
        steth,  # underlying asset
        treasury,  # treasury,
        "Aave interest bearing StETH",
        "aStETH",
        ZERO_ADDRESS,
        tx_params,
        publish_source=publish_source,
    )


def deploy_variable_debt_steth_impl(
    lending_pool, steth, tx_params, publish_source=False
):
    return VariableDebtStETH.deploy(
        lending_pool,  # lending pool,
        steth,  # underlying asset
        "Aave variable debt bearing StETH",
        "variableDebtStETH",
        ZERO_ADDRESS,
        tx_params,
        publish_source=publish_source,
    )


def deploy_stable_debt_steth_impl(lending_pool, steth, tx_params, publish_source=False):
    return StableDebtStETH.deploy(
        lending_pool,  # lending pool,
        steth,  # underlying asset
        "Aave stable debt bearing StETH",
        "stableDebtStETH",
        ZERO_ADDRESS,
        tx_params,
        publish_source=publish_source,
    )


def deploy_steth_intereset_rate_strategy(tx_params, publish_source=False):
    return DefaultReserveInterestRateStrategy.deploy(
        aave.LENDING_POOL_ADDRESS_PROVIDER,
        constants.STRATEGY_STETH["optimalUtilizationRate"],
        constants.STRATEGY_STETH["baseVariableBorrowRate"],
        constants.STRATEGY_STETH["variableRateSlope1"],
        constants.STRATEGY_STETH["variableRateSlope2"],
        constants.STRATEGY_STETH["stableRateSlope1"],
        constants.STRATEGY_STETH["stableRateSlope2"],
        tx_params,
        publish_source=publish_source,
    )
