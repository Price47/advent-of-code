import os
from functools import reduce
from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class Submarine(AOCBase):

    def __init__(self):
        self.depth=0
        self.horizontal=0
        self.aim=0

    def dive(self, n):
        self.depth += n

    def adjust_aim(self, n):
        self.aim += n

    def drive(self, n):
        self.horizontal += n

    def aimed_drive(self, n):
        self.drive(n)
        self.depth += self.aim * n


    def initiate_dive(self, data, commands):
        for line in data:
            c, n = line.split(' ')
            commands[c](int(n))

    def easy_dive(self, data):
        dive_inputs = {'forward': lambda n: self.drive(n),
                       'down': lambda n: self.dive(n),
                       'up': lambda n: self.dive(-n)}

        self.initiate_dive(data, dive_inputs)
        return self.depth * self.horizontal

    def aimed_dive(self, data):
        commands = {'forward': lambda n: self.aimed_drive(n),
                    'down': lambda n: self.adjust_aim(n),
                    'up': lambda n: self.adjust_aim(-n)}

        self.initiate_dive(data, commands)
        return self.depth * self.horizontal

    def run(self, data=None):
        data = data or self.read_input()
        log.info(f"Simple dive position: {self.easy_dive(data)}")
        log.info(f"Dive position: {self.aimed_dive(data)}")
