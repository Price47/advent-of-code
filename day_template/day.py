from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):

    def run(self, data=None):
        data = data or self.read_input()

