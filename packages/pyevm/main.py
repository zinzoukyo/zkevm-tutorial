import utils.opcodes as opcodes
from vm import stack, flow, arith, comparison
class EVM:
    def __init__(self, code) -> None:
        self.code = code
        self.pc = 0
        self.stack = []
    
    # Program Counter Return Execute Opcodes
    def next(self):
        opCode = self.code[self.pc]
        self.pc += 1
        return opCode

    # Run EVM until code end
    def execute(self):
        while self.pc < len(self.code):
            opCode = self.next()

            # stack operations
            if opcodes.PUSH0 <= opCode and opcodes.PUSH32 or \
                opcodes.POP == opCode or \
                opcodes.DUP1 <= opCode and opcodes.DUP16 or \
                opcodes.SWAP1 <= opCode and opcodes.SWAP16:
                stack.Stack(self, evm, opCode)
            
            # flow operations
            elif opcodes.JUMP <= opCode and opCode <= opcodes.JUMPDEST:
                flow.Flow(self, evm, opCode)

            # arithmetic operations
            elif opcodes.ADD <= opCode and opCode <= opcodes.SIGNEXTEND:
                arith.Arithmetic(self, evm, opCode)

            # stop
            elif opcodes.STOP == opCode:
                break

            # comparison & bitwise logic operations
            elif opcodes.LT <= opCode and opCode <= opcodes.XOR:
                comparison.Comparison(self, evm, opCode)
# main
if __name__ == '__main__':
    code =  b"\x60\x01\x60\x01\x50"
    print(code)
    evm = EVM(code)
    evm.execute()
    print(evm.stack)