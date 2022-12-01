class Squid:

    def __init__(self, n):
        self.n = int(n)
        self.flashed = False

    def add_energy(self, n=1):
        self.n += n
        if self.n > 9:
            self.n = 0
            if not self.flashed:
                self.flashed = True
                return 1

        return 0

    def unflash(self):
        self.flashed = False

    def __add__(self, other):
        self.n += other

    def __lt__(self, other):
        return int(self.n) < other

    def __gt__(self, other):
        return int(self.n) > other

    def __eq__(self, other):
        return  int(self.n) == other


if __name__ == '__main__':
    s = Squid(1)
    assert s < 2