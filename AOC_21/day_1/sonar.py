import os
from functools import reduce
from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class Sonar(AOCBase):

    def sonar(self, data):
        return sum([1 for idx, d in enumerate(data) if d > data[idx-1]])

    def sonar_window(self, data):
        return sum([1 for i in range(len(data)) if sum(data[i+1:i+4]) > sum(data[i:i+3])])

    def run(self, data=None):
        data = data or self.read_input(int)
        log.info(f"Sonar sweep is {self.sonar(data)}")
        log.info(f"Sonar window sweep is {self.sonar_window(data)}")



