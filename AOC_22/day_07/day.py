from core import DefaultLogger, AOCBase
from AOC_22.device import Device


class day(AOCBase):
    def run(self):
        d = Device(terminal_input=self.data)
        d.parse_terminal_screen()

