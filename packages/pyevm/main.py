import utils.opcodes as opcodes
from vm import ( 
    stack, 
    arith, 
    comparison, 
    sha3env, 
    block,
    storage, 
    flow, 
    log,
    system 
)

class EVM:
    def __init__(self, code) -> None:
        self.code = code
        self.pc = 0
        self.stack = []
        self.memory = bytearray()
        self.storage = {}
    
    # Program Counter Return Execute Opcodes
    def next(self):
        opCode = self.code[self.pc]
        self.pc += 1
        return opCode

    # Run EVM until code end
    def execute(self):
        while self.pc < len(self.code):
            opCode = self.next()
            # stack operations (50, 5F-7F, 80-8F, 90-9F)
            if opcodes.PUSH0 <= opCode and opcodes.PUSH32 or \
                opcodes.POP == opCode or \
                opcodes.DUP1 <= opCode and opcodes.DUP16 or \
                opcodes.SWAP1 <= opCode and opcodes.SWAP16:
                stack.Stack(self, opCode)
            
            # stop operations (00)
            elif opcodes.STOP == opCode:
                break

            # arithmetic operations (01-0B)
            elif opcodes.ADD <= opCode and opCode <= opcodes.SIGNEXTEND:
                arith.Arithmetic(self, opCode)

            # comparison & bitwise logic operations (10-1D)
            elif opcodes.LT <= opCode and opCode <= opcodes.SAR:
                comparison.Comparison(self, opCode)

            # sha3 & enviroment operations (20, 30-3F)
            elif opcodes.SHA3 <= opCode and opCode <= opcodes.EXTCODECOPY:
                sha3env.Sha3Env(self, opCode)
            
            # block operations (40-48)
            elif opcodes.BLOCKHASH <= opCode and opCode <= opcodes.BASEFEE:
                block.Block(self, opCode)
            
            # memory & stack operations (51-55)
            elif opcodes.MLOAD <= opCode and opCode <= opcodes.SSTORE:
                storage.Storage(self, opCode)

            # flow operations (56-5B)
            elif opcodes.JUMP <= opCode and opCode <= opcodes.JUMPDEST:
                flow.Flow(self, opCode)
            
            # log operations (A0-A4)
            elif opcodes.LOG0 <= opCode and opCode <= opcodes.LOG4:
                log.Log(self, opCode)

            # system operations (F0-FF)
            elif opcodes.CREATE <= opCode and opCode <= opcodes.SELFBALANCE:
                system.System(self, opCode)
# main
if __name__ == '__main__':
    code =  b"\x40"
    evm = EVM(code)
    evm.execute()
    print(evm.stack)