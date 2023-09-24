#
# Comparison and Bitwise Logic
#
LT = 0x10
GT = 0x11
SLT = 0x12
SGT = 0x13
EQ = 0x14
ISZERO = 0x15
AND = 0x16
OR = 0x17
XOR = 0x18
NOT = 0x19
BYTE = 0x1A
SHL = 0x1B
SHR = 0x1C
SAR = 0x1D

class Comparison:
    def __init__(self, evm, opcodes) -> None:
        self.evm = evm
        if opcodes == LT:
            self.lt()
        elif opcodes == GT:
            self.gt()
        elif opcodes == SLT:
            self.lt()
        elif opcodes == SGT:
            self.gt()
        elif opcodes == EQ:
            self.eq()
        elif opcodes == ISZERO:
            self.iszero()
        elif opcodes == AND:
            self.and_()
        elif opcodes == OR:
            self.or_()
        elif opcodes == XOR:
            self.xor()
        elif opcodes == NOT:
            self.not_()
        elif opcodes == BYTE:
            self.byte()
        elif opcodes == SHL:
            self.shl()
        elif opcodes == SHR:
            self.shr()
        elif opcodes == SAR:
            self.sar()
    
    def lt(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = 1 if value2 < value1 else 0
        self.evm.stack.append(result)

    def gt(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = 1 if value2 > value1 else 0
        self.evm.stack.append(result)

    def eq(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = 1 if value2 == value1 else 0
        self.evm.stack.append(result)
    
    def iszero(self):
        value = self.evm.stack.pop()
        result = 1 if value == 0 else 0
        self.evm.stack.append(result)

    def and_(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value1 & value2
        self.evm.stack.append(result)

    def or_(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value1 | value2
        self.evm.stack.append(result)

    def xor(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value1 ^ value2
        self.evm.stack.append(result)

    def not_(self):
        value = self.evm.stack.pop()
        result = ~value
        self.evm.stack.append(result)

    def byte(self):
        position = self.evm.stack.pop()
        value = self.evm.stack.pop()
        result = (value >> (position * 8)) & 0xff
        self.evm.stack.append(result)
    
    def shl(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value2 << value1
        self.evm.stack.append(result)

    def shr(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value2 >> value1
        self.evm.stack.append(result)
    
    def sar(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value2 >> value1
        self.evm.stack.append(result)