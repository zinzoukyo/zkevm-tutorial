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

#
# Duplicate Operations
#
DUP1 = 0x80
DUP2 = 0x81
DUP3 = 0x82
DUP4 = 0x83
DUP5 = 0x84
DUP6 = 0x85
DUP7 = 0x86
DUP8 = 0x87
DUP9 = 0x88
DUP10 = 0x89
DUP11 = 0x8A
DUP12 = 0x8B
DUP13 = 0x8C
DUP14 = 0x8D
DUP15 = 0x8E
DUP16 = 0x8F

#
# Exchange Operations
#
SWAP1 = 0x90
SWAP2 = 0x91
SWAP3 = 0x92
SWAP4 = 0x93
SWAP5 = 0x94
SWAP6 = 0x95
SWAP7 = 0x96
SWAP8 = 0x97
SWAP9 = 0x98
SWAP10 = 0x99
SWAP11 = 0x9A
SWAP12 = 0x9B
SWAP13 = 0x9C
SWAP14 = 0x9D
SWAP15 = 0x9E
SWAP16 = 0x9F

class Stack:
    def __init__(self, evm, opCode) -> None:
        self.evm = evm
        if opCode == PUSH0:
            evm.stack.append(0)
        elif PUSH1 <= opCode and opCode <= PUSH32:
            size = opCode - PUSH1 + 1
            self.push(size)
        elif opCode == POP:
            self.pop()
        elif DUP1 <= opCode and opCode <= DUP16:
            position = opCode - DUP1 + 1
            self.dup(position)
        elif SWAP1 <= opCode and opCode <= SWAP16:
            position1 = opCode - SWAP1 + 1
            position2 = 1
            self.swap(position1, position2)
    
    def push(self, size):
        data = self.evm.code[self.evm.pc : self.evm.pc + size]
        value = int.from_bytes(data, byteorder='big')
        self.evm.stack.append(value)
        self.evm.pc += size

    def pop(self):
        return self.evm.stack.pop()
    
    def dup(self, position):
        value = self.evm.stack[-position]
        self.evm.stack.append(value)

    def swap(self, position1, position2):
        self.evm.stack[-position1], self.evm.stack[-position2] = self.evm.stack[-position2], self.evm.stack[-position1]