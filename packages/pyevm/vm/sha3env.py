#
# Sha3
#
SHA3 = 0x20

#
# Environment Information
#
ADDRESS = 0x30
BALANCE = 0x31
ORIGIN = 0x32
CALLER = 0x33
CALLVALUE = 0x34
CALLDATALOAD = 0x35
CALLDATASIZE = 0x36
CALLDATACOPY = 0x37
CODESIZE = 0x38
CODECOPY = 0x39
GASPRICE = 0x3A
EXTCODESIZE = 0x3B
EXTCODECOPY = 0x3C
RETURNDATASIZE = 0x3D
RETURNDATACOPY = 0x3E
EXTCODEHASH = 0x3F

import sha3

class Sha3Env:
    def __init__(self, evm, opCode) -> None:
        self.evm = evm
        if opCode == SHA3:
            self._sha3()
        elif opCode == ADDRESS:
            self.address()
        elif opCode == BALANCE:
            self.balance()
        elif opCode == ORIGIN:
            self.origin()
        elif opCode == CALLER:
            self.caller()
        elif opCode == CALLVALUE:
            self.callvalue()
        elif opCode == CALLDATALOAD:
            self.calldataload()
        elif opCode == CALLDATASIZE:
            self.calldatasize()
        elif opCode == CALLDATACOPY:
            self.calldatacopy()
        elif opCode == CODESIZE:
            self.codesize()
        elif opCode == CODECOPY:
            self.codecopy()
        elif opCode == GASPRICE:
            self.gasprice()
        elif opCode == EXTCODESIZE:
            self.extcodesize()
        elif opCode == EXTCODECOPY:
            self.extcodecopy()
        elif opCode == RETURNDATASIZE:
            self.returndatasize()
        elif opCode == RETURNDATACOPY:
            self.returndatacopy()
        elif opCode == EXTCODEHASH:
            self.extcodehash()
    
    def _sha3(self):
        data_start = self.evm.stack.pop()
        data_length = self.evm.stack.pop()
        data = self.evm.memory[data_start:data_start + data_length]
        result = int.from_bytes(sha3.keccak_256(data).digest(), 'big')
        self.evm.stack.append(result)

    def address(self):
        self.evm.stack.append(self.evm.address)

    def balance(self):
        address = self.evm.stack.pop()
        self.evm.stack.append(self.evm.balance(address))

    def origin(self):
        self.evm.stack.append(self.evm.origin)
    
    def caller(self):
        self.evm.stack.append(self.evm.caller)

    def callvalue(self):
        self.evm.stack.append(self.evm.callvalue)

    def calldataload(self):
        position = self.evm.stack.pop()
        result = self.evm.calldata[position:position + 32]
        self.evm.stack.append(result)

    def calldatasize(self):
        self.evm.stack.append(len(self.evm.calldata))

    def calldatacopy(self):
        mem_start = self.evm.stack.pop()
        data_start = self.evm.stack.pop()
        data_length = self.evm.stack.pop()
        self.evm.memory[mem_start:mem_start + data_length] = self.evm.calldata[data_start:data_start + data_length]

    def codesize(self):
        self.evm.stack.append(len(self.evm.code))

    def codecopy(self):
        mem_start = self.evm.stack.pop()
        code_start = self.evm.stack.pop()
        code_length = self.evm.stack.pop()
        self.evm.memory[mem_start:mem_start + code_length] = self.evm.code[code_start:code_start + code_length]

    def gasprice(self):
        self.evm.stack.append(self.evm.gasprice)

    def extcodesize(self):
        address = self.evm.stack.pop()
        self.evm.stack.append(len(self.evm.extcodesize(address)))

    def extcodecopy(self):
        address = self.evm.stack.pop()
        mem_start = self.evm.stack.pop()
        code_start = self.evm.stack.pop()
        code_length = self.evm.stack.pop()
        self.evm.memory[mem_start:mem_start + code_length] = self.evm.extcodecopy(address, code_start, code_length)

    def returndatasize(self):
        self.evm.stack.append(len(self.evm.returndata))

    def returndatacopy(self):
        mem_start = self.evm.stack.pop()
        data_start = self.evm.stack.pop()
        data_length = self.evm.stack.pop()
        self.evm.memory[mem_start:mem_start + data_length] = self.evm.returndata[data_start:data_start + data_length]

    def extcodehash(self):
        address = self.evm.stack.pop()
        code = self.get_code_at_address(address)
        code_hash = sha3(code)
        self.evm.stack.append(code_hash)

    def get_code_at_address(self, address):
        return '0x'