from core import DefaultLogger, AOCBase
from collections import defaultdict
import re


log = DefaultLogger.get_log()

class MemoryGame(AOCBase):
    """
    https://adventofcode.com/2020/day/13

    """
    def __init__(self):
        self.data = self.read_input(int)

    def play(self):
        x = 2020
        idx = 0
        while idx < x - 1: # 1 indexed turn spoken
            n = self.data[-1]
            if n in self.data[0:-1]:
                for i in range(len(self.data) - 2, -1, -1):
                    if self.data[i] == n:
                        self.data.append(len(self.data) - 1 - i)
                        break
            else:
                self.data.append(0)


            idx += 1
            log.debug(idx)

        print(self.data)

        print(self.data[x-1])


    def main(self):
        self.play()

