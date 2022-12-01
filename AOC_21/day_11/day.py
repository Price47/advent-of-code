from core import DefaultLogger, AOCBase
from .squid import Squid


log = DefaultLogger().get_log()


class day(AOCBase):
    def __init__(self, data=None):
        self.data = [[Squid(int(n)) for n in row] for row in data or self.read_input()]
        self.flashes = 0

    def adjacent_energy(self, x, y):
        sum = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                try:
                    if y+dy < 0 or x+dx < 0:
                        continue
                    if self.data[y+dy][x+dx] == 0:
                        sum += 1
                except IndexError:
                    pass

        return sum

    def iter_squid(self, fn):
        for squid_row in self.data:
            for squid in squid_row:
                fn(squid)

    def _check_flashed(self):
        pass

    def _unflash(self, s: Squid):
        s.unflash()

    def _flash(self, s: Squid):
        if s > 0: self.flashes += s.add_energy()

    def flash_wave(self):
        flashes = 0
        for y, squid_row in enumerate(self.data):
            for x, squid in enumerate(squid_row):
                flashes += squid.add_energy(self.adjacent_energy(x, y))

        self.flashes += flashes
        return flashes

    def unflash_all(self):
        self.iter_squid(self._unflash)

    def flash_step(self):
        self.iter_squid(self._flash)
        new_flashes = self.flash_wave()
        while new_flashes > 0:
            new_flashes = self.flash_wave()
        self.unflash_all()




    def run(self):
        for i in range(100):
            self.flash_step()
            print(self.flashes)

