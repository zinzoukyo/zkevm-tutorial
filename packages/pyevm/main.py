import opcodes
from vm import stack

class EVM:
    def __init__(self, code) -> None:
        self.code = code
        self.pc = 0
        self.stack = []
    
    def next(self):
        opCode = self.code[self.pc]
        self.pc += 1
        return opCode

    def execute(self):
        while self.pc < len(self.code):
            opCode = self.next()

            # stack operations
            if opcodes.PUSH0 <= opCode and opcodes.PUSH32 or opCode == opcodes.POP:
                stack.Stack(self, opCode)
              

# main
if __name__ == '__main__':
    code =  b"\x60\x01\x60\x01\x50"
    evm = EVM(code)
    evm.execute()
    print(evm.stack)