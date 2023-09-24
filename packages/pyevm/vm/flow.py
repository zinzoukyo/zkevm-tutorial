#
# Memory, Storage and Flow Operations
#

JUMP = 0x56
JUMPI = 0x57
PC = 0x58
MSIZE = 0x59
GAS = 0x5A
JUMPDEST = 0x5B

class Flow:
    def __init__(self, evm, opCode) -> None:
        self.evm = evm
        if opCode == JUMP:
            dst = self.evm.stack.pop()
            self.jump(dst)
        elif opCode == JUMPI:
            dst = self.evm.stack.pop()
            condition = self.evm.stack.pop()
            self.jumpi(dst, condition)
        elif opCode == PC:
            self.pc()
        elif opCode == MSIZE:
            self.msize()
        # elif opCode == GAS:
        #     self.gas()
        elif opCode == JUMPDEST:
            pass
        
    def jump(self, position):
        self.evm.pc = position
    
    def jumpi(self, jump_position, condition):
        if condition:
            self.evm.pc = jump_position

    def msize(self):
        self.evm.stack.append(len(self.evm.stack))
    
    def pc(self):
        self.evm.stack.append(self.evm.pc)