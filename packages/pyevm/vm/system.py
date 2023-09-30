import random
import sha3
from ..main import EVM
#
# System
#
CREATE = 0xF0
CALL = 0xF1
CALLCODE = 0xF2
RETURN = 0xF3
DELEGATECALL = 0xF4
CREATE2 = 0xF5
STATICCALL = 0xFA
REVERT = 0xFD
SELFDESTRUCT = 0xFF

class System:
    def __init__(self, evm, opCode, txn) -> None:
        self.evm = evm
        self.evm_account = []

    def create(self, txn):
        value = self.evm.stack.pop()
        mem_posision = self.evm.stack.pop()
        length = self.evm.stack.pop()

        init_code = self.memory[mem_posision: mem_posision + length]

        creator = self.getAccount(txn.origin)
        creator['balance'] -= value

        contract_addr_bytes = sha3(self.txn.thisAddr.encode() + str(creator['nonce']).encode()).digest()
        new_contract_address = '0x' + contract_addr_bytes[-20:].hex() 

        creator['nonce'] += 1

        self.evm_account[new_contract_address] = {
            'balance': value,
            'nonce': 0, 
            'storage': {},
            'code': init_code
        }
        
        self.evm.stack.append(int(new_contract_address, 16))

    def create2(self, txn, salt):
        value = self.evm.stack.pop()
        mem_posision = self.evm.stack.pop()
        length = self.evm.stack.pop()

        init_code = self.memory[mem_posision: mem_posision + length]

        creator = self.getAccount(txn.origin)
        creator['balance'] -= value

        init_code_hash = sha3(init_code).digest()
        data_to_hash = b'\xff' + self.txn.thisAddr.encode() + str(salt).encode() + init_code_hash
        contract_addr_bytes = sha3(data_to_hash).digest()
        new_contract_address = '0x' + contract_addr_bytes[-20:].hex()

        creator['nonce'] += 1

        self.evm_account[new_contract_address] = {
            'balance': value,
            'nonce': 0, 
            'storage': {},
            'code': init_code
        }
        
        self.evm.stack.append(int(new_contract_address, 16))

    def getAccount(self):
        return {
          'balance': random.randint(10, 50),
          'nonce': random.randint(0, 50),
        }

    def _call(self, txn):
        gas = self.evm.stack.pop()
        to = self.evm.stack.pop()
        value = self.evm.stack.pop()
        mem_start = self.evm.stack.pop()
        mem_length = self.evm.stack.pop()
        returndata_start = self.evm.stack.pop()
        returndata_length = self.evm.stack.pop()


        data = self.evm.memory[mem_start: mem_start + mem_length]
        
        source = self.getAccount(txn.caller)
        target = self.getAccount(hex(to))

        source['balance'] -= value
        target['balance'] += value
         
        # skip build tx and send tx

        self.evm.excute(target['code'])

        evm = EVM(target['code'])
        evm.memory = data
        evm.execute()

        self.evm.memory[returndata_start:returndata_start + returndata_length] = evm.stack

    def callcode(self):
        self._call()

    def delegatecall(self, txn):
        gas = self.evm.stack.pop()
        to = self.evm.stack.pop()
        mem_start = self.evm.stack.pop()
        mem_length = self.evm.stack.pop()
        returndata_start = self.evm.stack.pop()
        returndata_length = self.evm.stack.pop()


        data = self.evm.memory[mem_start: mem_start + mem_length]
        
        target = self.getAccount(hex(to))
         
        # skip build tx and send tx

        self.evm.excute(target['code'])

        evm = EVM(target['code'])
        evm.memory = data
        evm.storage = self.evm.storage
        evm.execute()

        self.evm.memory[returndata_start:returndata_start + returndata_length] = evm.stack

    def staticcall(self):
        gas = self.evm.stack.pop()
        to = self.evm.stack.pop()
        mem_start = self.evm.stack.pop()
        mem_length = self.evm.stack.pop()
        returndata_start = self.evm.stack.pop()
        returndata_length = self.evm.stack.pop()

        data = self.evm.memory[mem_start: mem_start + mem_length]

        target = self.getAccount(hex(to))

        self.evm.excute(target['code'])

        self.evm.memory[returndata_start:returndata_start + returndata_length] = self.evm.stack

    def _return(self):
        mem_start = self.evm.stack.pop()
        mem_length = self.evm.stack.pop()

        self.evm.stack = self.evm.memory[mem_start: mem_start + mem_length]

    def revert(self):
        mem_start = self.evm.stack.pop()
        mem_length = self.evm.stack.pop()

        self.evm.stack = self.evm.memory[mem_start: mem_start + mem_length]
        self.success = False

    def selfdestruct(self, txn):
        to = self.evm.stack.pop()
        target = self.getAccount(hex(to))

        self.evm.balance[txn.thisAddr] += target['balance']
        target['balance'] = 0

