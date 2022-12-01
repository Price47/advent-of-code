from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()

    def run(self):
        pass

