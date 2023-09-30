import random
import time

class Fakeblock:
    # return a fake block dict
    def __init__(self) -> None:
        self.blockhash = self._generate_hash()
        self.coinbase = self._generate_address()
        self.timestamp = int(time.time())  # 獲取當前時間戳
        self.number = random.randint(1, 20000000)  # 隨機生成區塊編號
        self.prevrandao = self._generate_hash()
        self.gaslimit = random.randint(10, 50)
        self.chainid = 1
        self.selfbalance = random.randint(50, 150)
        self.basefee = random.randint(10, 50)
        self.difficulty = random.randint(10, 50)
        self.blockinfo = self.to_dict()

    def _generate_hash(self):
        return "0x" + "".join(random.choice("0123456789abcdef") for _ in range(64))

    def _generate_address(self):
        return "0x" + "".join(random.choice("0123456789abcdef") for _ in range(40))

    def to_dict(self):
        return {
            "blockhash": self.blockhash,
            "coinbase": self.coinbase,
            "timestamp": self.timestamp,
            "number": self.number,
            "prevrandao": self.prevrandao,
            "gaslimit": self.gaslimit,
            "chainid": self.chainid,
            "selfbalance": self.selfbalance,
            "basefee": self.basefee,
            "difficulty": self.difficulty
        }