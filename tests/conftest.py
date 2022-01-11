import pytest


@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    """Snapshot ganache before every test function call."""
    pass


############
# EOA
############


@pytest.fixture(scope="module")
def deployer(accounts):
    return accounts[0]
