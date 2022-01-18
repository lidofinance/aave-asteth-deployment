from scripts import deploy
from utils import aave, deployment, lido, constants


def test_deployment(deployer):
    lending_pool_address = aave.lending_pool_address_provider().getLendingPool()
    (
        asteth_impl,
        stable_debt_steth_impl,
        variable_debt_steth_impl,
        steth_interest_rate_strategy,
    ) = deploy.deploy_implementation_and_strategy(
        lending_pool_address, {"from": deployer}
    )
    validate_asteth_impl(asteth_impl, lending_pool_address)
    validate_stable_debt_steth_impl(stable_debt_steth_impl, lending_pool_address)
    validate_variable_debt_steth_impl(variable_debt_steth_impl, lending_pool_address)
    validate_steth_interest_rate_strategy(steth_interest_rate_strategy)


def validate_steth_interest_rate_strategy(strategy):
    strategy_config = constants.STRATEGY_STETH
    assert (
        strategy.OPTIMAL_UTILIZATION_RATE() == strategy_config["optimalUtilizationRate"]
    )
    assert (
        strategy.EXCESS_UTILIZATION_RATE()
        == constants.ONE_RAY - strategy_config["optimalUtilizationRate"]
    )
    assert strategy.variableRateSlope1() == strategy_config["variableRateSlope1"]
    assert strategy.variableRateSlope2() == strategy_config["variableRateSlope2"]
    assert strategy.stableRateSlope1() == strategy_config["stableRateSlope1"]
    assert strategy.stableRateSlope2() == strategy_config["stableRateSlope2"]
    assert (
        strategy.baseVariableBorrowRate() == strategy_config["baseVariableBorrowRate"]
    )


def validate_asteth_impl(asteth_impl, lending_pool_address):
    assert asteth_impl.UNDERLYING_ASSET_ADDRESS() == lido.STETH_ADDRESS
    assert asteth_impl.RESERVE_TREASURY_ADDRESS() == aave.TREASURY_ADDRESS
    assert asteth_impl.POOL() == lending_pool_address
    assert asteth_impl.name() == "Aave interest bearing STETH"
    assert asteth_impl.decimals() == 18
    assert asteth_impl.symbol() == "aSTETH"


def validate_stable_debt_steth_impl(stable_debt_steth_impl, lending_pool_address):
    assert stable_debt_steth_impl.UNDERLYING_ASSET_ADDRESS() == lido.STETH_ADDRESS
    assert stable_debt_steth_impl.POOL() == lending_pool_address
    assert stable_debt_steth_impl.name() == "Aave stable debt bearing STETH"
    assert stable_debt_steth_impl.decimals() == 18
    assert stable_debt_steth_impl.symbol() == "stableDebtSTETH"


def validate_variable_debt_steth_impl(variable_debt_steth_impl, lending_pool_address):
    assert variable_debt_steth_impl.UNDERLYING_ASSET_ADDRESS() == lido.STETH_ADDRESS
    assert variable_debt_steth_impl.POOL() == lending_pool_address
    assert variable_debt_steth_impl.name() == "Aave variable debt bearing STETH"
    assert variable_debt_steth_impl.decimals() == 18
    assert variable_debt_steth_impl.symbol() == "variableDebtSTETH"
