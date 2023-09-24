#
# Stop and Arithmetic
#
STOP = 0x00
ADD = 0x01
MUL = 0x02
SUB = 0x03
DIV = 0x04
SDIV = 0x05
MOD = 0x06
SMOD = 0x07
ADDMOD = 0x08
MULMOD = 0x09
EXP = 0x0A
SIGNEXTEND = 0x0B

class Arithmetic:
    def __init__(self, evm, opCode) -> None:
        self.evm = evm
        if opCode == ADD:
            self.add()
        elif opCode == MUL:
            self.mul()
        elif opCode == SUB:
            self.sub()
        elif opCode == DIV:
            self.div()
        elif opCode == SDIV:
            self.div()
        elif opCode == MOD:
            self.mod()
        elif opCode == SMOD:
            self.mod()
        elif opCode == ADDMOD:
            self.addmod()
        elif opCode == MULMOD:
            self.mulmod()
        elif opCode == EXP:
            self.exp()
        elif opCode == SIGNEXTEND:
            self.signextend()

    def add(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value1 + value2 
        self.evm.stack.append(result)

    def mul(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value1 * value2 
        self.evm.stack.append(result)

    def sub(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value1 - value2 
        self.evm.stack.append(result)

    def div(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value2 // value1 if value1 != 0 else 0
        self.evm.stack.append(result)

    def mod(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = value2 % value1 if value1 != 0 else 0
        self.evm.stack.append(result)

    def addmod(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        value3 = self.evm.stack.pop()
        result = (value1 + value2) % value3 if value3 != 0 else 0
        self.evm.stack.append(result)

    def mulmod(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        value3 = self.evm.stack.pop()
        result = (value1 * value2) % value3 if value3 != 0 else 0
        self.evm.stack.append(result)
    
    def exp(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        result = pow(value1, value2) 
        self.evm.stack.append(result)

    def signextend(self):
        value1 = self.evm.stack.pop()
        value2 = self.evm.stack.pop()
        sign_bit = 255 if value1 & 128 else 0
        result = (value2 & ((1 << (8 * value1)) - 1)) or \
            (sign_bit << (8 * value1))
        self.evm.stack.append(result)