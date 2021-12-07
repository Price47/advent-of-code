from core import DefaultLogger, AOCBase
from statistics import median

log = DefaultLogger().get_log()


class day(AOCBase):

    def crab_fuel_consumption(self, n, avg):
        return sum([i for i in range(abs(n-avg)+1)])

    def realignment(self, crab_subs):
        pivot = median(crab_subs)
        fuel_consumed = int(sum([abs(c - pivot) for c in crab_subs]))
        log.info(f"Total Fuel consumed {fuel_consumed}")

    def crab_realignment(self, crab_subs):
        avg = round(sum(crab_subs) // len(crab_subs))
        fuel_consumed = sum(
            [self.crab_fuel_consumption(c, avg) for c in crab_subs]
        )
        log.info(f"Total Fuel Consumed {fuel_consumed}")

    def run(self, data=None):
        data = data or self.read_input()
        crab_subs = sorted([int(n) for n in data[0].split(',')])

        self.realignment(crab_subs)
        self.crab_realignment(crab_subs)



