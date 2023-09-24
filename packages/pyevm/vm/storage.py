MLOAD = 0x51
MSTORE = 0x52
MSTORE8 = 0x53
SLOAD = 0x54
SSTORE = 0x55

class Storage:
    def __init__(self, evm, opCode) -> None:
        self.evm = evm
        self.memory = evm.memory
        if opCode == MLOAD:
            self.mload()
        elif opCode == MSTORE:
            self.mstore()
        elif opCode == MSTORE8:
            self.mstore8()
        elif opCode == SLOAD:
            self.sload()
        elif opCode == SSTORE:
            self.sstore()