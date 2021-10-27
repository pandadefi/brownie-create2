import pytest
from eth_utils import keccak, to_checksum_address
import secrets


def test_factory_computeAddress(user, factory, Test):
    salt = secrets.token_bytes(32).hex()
    init_code = Test.bytecode

    b_init_code = bytes.fromhex(init_code)
    keccak_b_init_code = keccak(b_init_code).hex()
    tx = factory.deploy(init_code, salt)
    contract_address = tx.events["Deployed"]["deployed"]
    assert factory.computeAddress(keccak_b_init_code, salt) == contract_address

    test = Test.at(contract_address)
    assert test.alive() == True

def test_factory_local_pre_compute(user, factory, Test):
    salt = secrets.token_bytes(32).hex()
    init_code = Test.bytecode

    pre = "0xff"
    b_pre = bytes.fromhex(pre[2:])
    b_address = bytes.fromhex(factory.address[2:])
    b_salt = bytes.fromhex(salt)
    b_init_code = bytes.fromhex(init_code)
    keccak_b_init_code = keccak(b_init_code)
    b_result = keccak(b_pre + b_address + b_salt + keccak_b_init_code)
    result_address = to_checksum_address(b_result[12:].hex())

    tx = factory.deploy(init_code, salt)
    contract_address = tx.events["Deployed"]["deployed"]

    assert contract_address == result_address
    test = Test.at(contract_address)
    assert test.alive() == True
