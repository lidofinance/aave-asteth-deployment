import brownie
from scripts.initialize import (
    initialize_asteth_impl,
    initialize_stable_debt_steth_impl,
    initialize_variable_debt_steth_impl,
)


def test_initialize(deployer):
    tx_params = {"from": deployer}
    asteth_impl = initialize_asteth_impl(tx_params)
    assert asteth_impl.decimals() == 18
    assert asteth_impl.name() == "Aave interest bearing STETH"
    assert asteth_impl.symbol() == "aSTETH"
    with brownie.reverts("Contract instance has already been initialized"):
        initialize_asteth_impl(tx_params)

    stable_debt_steth_impl = initialize_stable_debt_steth_impl(tx_params)
    assert stable_debt_steth_impl.decimals() == 18
    assert stable_debt_steth_impl.name() == "Aave stable debt bearing STETH"
    assert stable_debt_steth_impl.symbol() == "stableDebtSTETH"
    with brownie.reverts("Contract instance has already been initialized"):
        initialize_stable_debt_steth_impl(tx_params)

    variable_debt_steth_impl = initialize_variable_debt_steth_impl(tx_params)
    assert variable_debt_steth_impl.decimals() == 18
    assert variable_debt_steth_impl.name() == "Aave variable debt bearing STETH"
    assert variable_debt_steth_impl.symbol() == "variableDebtSTETH"
    with brownie.reverts("Contract instance has already been initialized"):
        initialize_variable_debt_steth_impl(tx_params)
