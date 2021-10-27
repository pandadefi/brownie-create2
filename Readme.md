# Brownie create2

Simple example contract to deploy a contract using create2.

## Deployed Factories


## How can I use this project

You don't have to clone this repo code, you only need a properly setup brownie environement.

First you will have to find a `salt` that gives your contract a [more efficient address](https://medium.com/coinmonks/on-efficient-ethereum-addresses-3fef0596e263).

In order to find the we will use [create2crunch](https://github.com/0age/create2crunch).


You can get the contract hash with the following code on a borwnie console:

```
from eth_utils import keccak
b_init_code = bytes.fromhex(Test.bytecode)
print(keccak(b_init_code).hex())
```


Once you have found the ideal salt:
```
salt = "ADD SOME SALT"
factory = Contract("FACTORY ADDRESS")
factory.deploy(factory, salt)
```

## Compute contract address

You can get the predicted contract using pure python or calling the contract computeAddress view function.
Examples can be found on the test file.


## Find efficient addresses to use

Check [create2crunch](https://github.com/0age/create2crunch) 