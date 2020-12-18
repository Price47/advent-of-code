import math

from core import DefaultLogger, AOCBase
from collections import defaultdict
import re


log = DefaultLogger.get_log()

class BusScheduler(AOCBase):
    """
    https://adventofcode.com/2020/day/13

    """
    def __init__(self):
        data = self.read_input()
        self.depart_time = int(data[0])
        self.buses = [b for b in data[1].split(',')]
        self.hours = [int(f'{h}{i if i>9 else self._pad(i)}') for h in range(24) for i in range(60)]

    def _pad(self, i):
        return f'0{i}'

    def bus_schedules(self):
        buses = [int(b) for b in self.buses if b != 'x']
        schedules = {b: [i for i in range(0, self.depart_time * 2, b)] for b in buses}

        return schedules

    def closest_time(self, schedule):
        for s in schedule:
            if s >= self.depart_time:
                return s

    def find_departure_time(self):
        schedules = self.bus_schedules()
        closest_bus_departures = []

        for bus, schedule in schedules.items():
            closest_bus_departures.append((bus, self.closest_time(schedule)))

        return closest_bus_departures

    def best_departure_time(self):
        closest_departure_time = self.find_departure_time()
        b = {d: b for b, d in closest_departure_time}

        wait_time = min([d[1] - self.depart_time for d in closest_departure_time])
        bus_id = b[wait_time + self.depart_time]

        log.info(f"Best departure time is bus {bus_id} [ {wait_time * bus_id} ]")

    def _check_subsequent(self, t, buses):
        offset, bus = buses[0]
        if (t + offset) % bus == 0:
            if len(buses) > 1:
                return self._check_subsequent(t, buses[1:])
            else:
                return True
        else:
            return False

    def subsequent_departures(self):
        d = [(i, v) for i, v in enumerate(self.read_input()[1].split(','))]
        buses = [(i, int(v)) for i, v in filter(lambda x: x[1] != 'x', d)]
        timestamp_subsequent = False
        t = 0
        while not timestamp_subsequent:
            log.debug(f'timestamp {t}')
            timestamp_subsequent = self._check_subsequent(t, buses)
            if timestamp_subsequent:
                return t
            t += 1

    def ExtendedEuclid(self, x, y):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while y > 0:
            q, x, y = math.floor(x / y), y, x % y
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return x0, y0  # gcd and the two coefficients

    def invmod(self, a, m):
        x, _ = self.ExtendedEuclid(a, m)
        return x % m

    def ChineseRemainderGauss(self, n, N, a):
        result = 0
        for i in range(len(n)):
            ai = a[i]
            ni = n[i]
            bi = N // ni
            result += ai * bi * self.invmod(bi, ni)
        return result % N

    def subsequent_departures_crt(self):
        """
        https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
        https://medium.com/@astartekraus/the-chinese-remainder-theorem-ea110f48248c
        :return:
        """
        # order by modulo descending
        departures =  [(i, int(v)) for i, v in enumerate(self.read_input()[1].split(',')) if v != 'x']
        sorted_departures = sorted(departures, key=lambda x: x[0], reverse=True)
        print(sorted_departures)

        t, increment = 0, sorted_departures[0][1]
        for offset, time in sorted_departures[1:]:
            log.debug(f'timestamp {t}')
            while (t + offset) % time != 0:
                t += increment

            increment *= time

        return t

    def main(self):
        # self.best_departure_time()
        log.info(self.subsequent_departures_crt())

