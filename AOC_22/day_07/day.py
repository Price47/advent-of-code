from core import DefaultLogger, AOCBase
from AOC_22.device import Device



# log = DefaultLogger().get_log()


class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()

    def run(self):
        d = Device(terminal_input=self.data)
        d.parse_terminal_screen()

