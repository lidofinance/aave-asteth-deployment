# AAVE StETH Integration Deployment

The repository contains scripts for deployment and verification of the implementation of the StETH integration on AAVE.

## Project Setup

To use the tools provided by this project, please pull the repository from GitHub and install
its dependencies as follows. It is recommended to use a Python virtual environment.

```bash
git clone https://github.com/lidofinance/aave-asteth-deployment
cd aave-asteth-deployment
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements-dev.txt
```

To run scripts and tests in this repo, store your project ID as an environment variable named WEB3_INFURA_PROJECT_ID. You can do so with the following command:

```bash
$ export WEB3_INFURA_PROJECT_ID=YourProjectID
```

Note that for correct work of scripts you have to have exact the "1.17.0" version of the eth-brownie package.

## Deployment

To run deployment use the command `DEPLOYER=<DEPLOYER_ACCOUNT> brownie run deploy`. This command will deploy contracts required for StETH listing on AAVE:

- AStETH.sol (SHA-256 hash: 0x7e86a48c1d4b43a5e4ebca7d44704a6ef273a93ba049e9c1cd19cb512da12b98)
- VariableDebtStETH.sol (SHA-256 hash: 0xa6461b9f089d5a8f64edef1d37523ddb11e2973f1ea2f2996961f61e83c5a969)
- StableDebtStETH.sol (SHA-256 hash: 0x7e86a48c1d4b43a5e4ebca7d44704a6ef273a93ba049e9c1cd19cb512da12b98)
- DefaultReserveInterestRateStrategy.sol (SHA-256 hash: 0x52e45a1e4d0969524a362cabb4370176303b62d511ba2321e95d37c49287fdab)

## Bytecode Checking

To validate that bytecode of contracts deployed in the mainnet network matches the bytecode of contracts deployed via scripts from this repo, you can use the command `brownie run check_bytecode`. This command will do the next steps to validate the bytecode of the deployed contracts:

1. Download bytecode of contracts deployed in the mainnet via JSON-RPC call to Ethereum node.
2. Deploy contracts in the mainnet fork via scripts in this repo.
3. Download bytecode of newly deployed contracts from the mainnet fork via JSON-RPC call.
4. Compare that bytecode of previously and newly deployed contracts match.

## Tests

To run the acceptance test use the command `brownie test -s`.
