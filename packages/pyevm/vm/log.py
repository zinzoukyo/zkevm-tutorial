#
# Logging
#
LOG0 = 0xA0
LOG1 = 0xA1
LOG2 = 0xA2
LOG3 = 0xA3
LOG4 = 0xA4


class Log:
    def __init__(self, evm, opCode) -> None:
        self.evm = evm
        self.memory = evm.memory
        if opCode == LOG0:
            self.log0()
        elif opCode == LOG1:
            self.log1()
        elif opCode == LOG2:
            self.log2()
        elif opCode == LOG3:
            self.log3()
        elif opCode == LOG4:
            self.log4()