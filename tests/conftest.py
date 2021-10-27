import pytest
from brownie import config


@pytest.fixture
def user(accounts):
    yield accounts[0]


@pytest.fixture
def factory(user, Factory):
    yield user.deploy(Factory)
