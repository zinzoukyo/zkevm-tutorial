# These opcodes seem to belong in the environment block,
# but we are out of opcode space in 0x3*
CHAINID = 0x46
SELFBALANCE = 0x47
BASEFEE = 0x48

#
# Block Information
#
BLOCKHASH = 0x40
COINBASE = 0x41
TIMESTAMP = 0x42
NUMBER = 0x43
DIFFICULTY = 0x44
PREVRANDAO = 0x44  # EIP-4399: supplant DIFFICULTY with PREVRANDAO
GASLIMIT = 0x45

from utils import fakeBlock
class Block:
    def __init__(self, evm, opCode) -> None:
        self.evm = evm
        block = fakeBlock.Fakeblock()
        self.block = block.blockinfo
        if opCode == CHAINID:
            self.chainid()
        elif opCode == SELFBALANCE:
            self.selfbalance()
        elif opCode == BASEFEE:
            self.basefee()
        elif opCode == BLOCKHASH:
            self.blockhash()
        elif opCode == COINBASE:
            self.coinbase()
        elif opCode == TIMESTAMP:
            self.timestamp()
        elif opCode == NUMBER:
            self.number()
        elif opCode == DIFFICULTY:
            self.difficulty()
        elif opCode == PREVRANDAO:
            self.prevrandao()
        elif opCode == GASLIMIT:
            self.gaslimit()

    def chainid(self):
        self.evm.stack.append(self.block["chainid"])
    
    def selfbalance(self):
        self.evm.stack.append(self.block["selfbalance"])

    def basefee(self):
        self.evm.stack.append(self.block["basefee"])

    def blockhash(self):
        # block_number = self.evm.stack.pop()
        self.evm.stack.append(self.block["blockhash"])
    
    def coinbase(self):
        self.evm.stack.append(self.block["coinbase"])

    def timestamp(self):
        self.evm.stack.append(self.block["timestamp"])

    def number(self):
        self.evm.stack.append(self.block["number"])
    
    def difficulty(self):
        self.evm.stack.append(self.block["difficulty"])

    def prevrandao(self):
        self.evm.stack.append(self.block["prevrandao"])

    def gaslimit(self):
        self.evm.stack.append(self.block["gaslimit"])
        