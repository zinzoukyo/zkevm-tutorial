#
# POP Operations
#
POP = 0x50
#
# Push Operations
#
PUSH0 = 0x5F
PUSH1 = 0x60
PUSH2 = 0x61
PUSH3 = 0x62
PUSH4 = 0x63
PUSH5 = 0x64
PUSH6 = 0x65
PUSH7 = 0x66
PUSH8 = 0x67
PUSH9 = 0x68
PUSH10 = 0x69
PUSH11 = 0x6A
PUSH12 = 0x6B
PUSH13 = 0x6C
PUSH14 = 0x6D
PUSH15 = 0x6E
PUSH16 = 0x6F
PUSH17 = 0x70
PUSH18 = 0x71
PUSH19 = 0x72
PUSH20 = 0x73
PUSH21 = 0x74
PUSH22 = 0x75
PUSH23 = 0x76
PUSH24 = 0x77
PUSH25 = 0x78
PUSH26 = 0x79
PUSH27 = 0x7A
PUSH28 = 0x7B
PUSH29 = 0x7C
PUSH30 = 0x7D
PUSH32 = 0x7F

class Stack:
    def __init__(self, evm, opCode) -> []:
        self.evm = evm
        if opCode == PUSH0:
            evm.stack.append(0)
        elif PUSH1 <= opCode and opCode <= PUSH32:
            size = opCode - PUSH1 + 1
            self.push(size)
        elif opCode == POP:
            self.pop()
    
    def push(self, size):
        data = self.evm.code[self.evm.pc : self.evm.pc + size]
        value = int.from_bytes(data, byteorder='big')
        self.evm.stack.append(value)
        self.evm.pc += size

    def pop(self):
        return self.evm.stack.pop()