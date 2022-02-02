ONE_RAY = 10 ** 27

STRATEGY_STETH = {
    "optimalUtilizationRate": 6 * ONE_RAY // 10,  # 0.6
    "baseVariableBorrowRate": 0,
    "variableRateSlope1": 8 * ONE_RAY // 100,  # 8%
    "variableRateSlope2": 2 * ONE_RAY,  # 200%
    "stableRateSlope1": 0,
    "stableRateSlope2": 0,
    "baseLTVAsCollateral": 7000,
    "liquidationThreshold": 7500,
    "liquidationBonus": 10750,
    "borrowingEnabled": False,
    "stableBorrowRateEnabled": False,
    "reserveDecimals": 18,
    "reserveFactor": 1000,
}

VALID_CONTRACT_HASHES = {
    "StableDebtStETH": "0x7e86a48c1d4b43a5e4ebca7d44704a6ef273a93ba049e9c1cd19cb512da12b98",
    "VariableDebtStETH": "0xa6461b9f089d5a8f64edef1d37523ddb11e2973f1ea2f2996961f61e83c5a969",
    "AStETH": "0xb30a0f9d1ae3852ae4d960784bc8a03723f59164c0f8c935d739ca71293d4c02",
    "DefaultReserveInterestRateStrategy": "0x52e45a1e4d0969524a362cabb4370176303b62d511ba2321e95d37c49287fdab",
}
