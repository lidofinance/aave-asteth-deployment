# AAVE StETH Integration Deployment

The repository contains scripts for deployment and verification of the implementation of the StETH integration on AAVE.

## Deployment

To run deployment use the command `DEPLOYER=<DEPLOYER_ACCOUNT> brownie run deploy`. This command will deploy contracts required for StETH listing on AAVE:

- AStETH.sol (SHA-256 hash: 0xeaf30bb7257d6a0d6c025ba81f5814bc48f80d521c6ded0f9b4bfad0e28ecaa1)
- VariableDebtStETH.sol (SHA-256 hash: 0xa6461b9f089d5a8f64edef1d37523ddb11e2973f1ea2f2996961f61e83c5a969)
- StableDebtStETH.sol (SHA-256 hash: 0x7e86a48c1d4b43a5e4ebca7d44704a6ef273a93ba049e9c1cd19cb512da12b98)
- DefaultReserveInterestRateStrategy.sol (SHA-256 hash: 0x52e45a1e4d0969524a362cabb4370176303b62d511ba2321e95d37c49287fdab)

## Tests

To run the acceptance test use the command `brownie test -s`.
