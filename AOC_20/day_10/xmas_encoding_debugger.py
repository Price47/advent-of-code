from core import DefaultLogger, AOCBase
from collections import defaultdict
import re


log = DefaultLogger.get_log()


class JoltageHandler(AOCBase):
    """
    https://adventofcode.com/2020/day/9

    """

    def __init__(self):
        super(JoltageHandler, self).__init__()
        self.joltages = sorted(self.read_input(int))
        joltage_chain = self.joltages + [max(self.joltages) + 3]
        self.joltage_adapters = {j: [j + i for i in range(1, 4) if j + i in joltage_chain] for j in joltage_chain[0:-1]}

    def check_adapters(self):
        data = self.read_input(int)

        adapters = defaultdict(list)
        effective_joltage_rating = 0

        joltages = sorted(data)
        device_joltage = max(data) + 3

        for joltage in joltages:
            for i in [1, 2, 3]:
                if joltage == effective_joltage_rating + i:
                    adapters[i].append(joltage)
                    effective_joltage_rating = joltage

        if effective_joltage_rating + 3 == device_joltage:
            adapters[3].append(device_joltage)
            return adapters

        log.error("couldn't reach device joltage")
        return {}

    def _check_arragnement(self, effective_joltage_rating, joltage, device_joltage, data, i=0):
        log.debug('checking arrangment')
        log.info(effective_joltage_rating)
        log.warning(joltage)
        log.info(effective_joltage_rating + i)

        if effective_joltage_rating + 3 == device_joltage:
            return 1

        if effective_joltage_rating + i > joltage:
            return 0

        for i in [1, 2, 3]:
            if effective_joltage_rating + i == joltage:
                return self._check_arragnement(effective_joltage_rating + i, joltage, device_joltage, data, i)

        return 0

    def _add_x(self, arrangement, key, addapter_joltages):
        if addapter_joltages.get(key):
            arrangement += addapter_joltages.get(key)
            return self._add_x(arrangement, key, addapter_joltages)
        else:
            return arrangement


    def _add_arrangements(self, key, arrangments, current_arrangement=[]):
        options = self.joltage_adapters.get(key)
        if not options:
            arrangments.append(current_arrangement)
            return []
        else:
            for option in options:
                current_arrangement.append(option)
                current_arrangement = self._add_arrangements(option, arrangments, current_arrangement)

        return []


    def arrangements(self):
        adapter_arrangements = []

        self._add_arrangements(self.joltages[0], adapter_arrangements)
        log.error(len(adapter_arrangements))
        #     # a.append(self._add_x([], key, acceptable_adapter_joltages))
        #     x = [key]
        #     options = acceptable_adapter_joltages[key]
        #     for option in options:
        #         options = acceptable_adapter_joltages[option]
        #         log.debug(option)
        #         log.error(options)
            # for xe in xes:
                # print(acceptable_adapter_joltages[xe])
            # if acceptable_adapter_joltages[key] in acceptable_adapter_joltages.keys():
            #     x += acceptable_adapter_joltages[key]
            # a.append(x)



        # print(a)

        # acceptable_adapter_joltages_in = set(acceptable_adapter_joltages) & set(joltages)

        # print()
        # print(acceptable_adapter_joltages_in)

        # device_joltage = max(data) + 3
        # arrangements = {}
        #
        # for i in range(len(joltages), 0 -1):
        #     arrangements[joltages[i]] = []
        #     for x in [1, 2, 3]:
        #         if joltages[i] - x == joltages[i-1]:
        #             arrangements[joltages[i]].append(joltages[i])
        #
        # print(arrangements)
        #     # effective_joltage_rating = 0
        #     # arrangements += self._check_arragnement(effective_joltage_rating, joltage, device_joltage, data)
        #
        # log.warning(arrangements)


    def main(self):
        adapters_list = self.check_adapters()
        log.debug(
            [f'[{len(val_list)}] {joltage_difference} joltage differences'
             for joltage_difference, val_list in adapters_list.items()]
        )

        log.info(f'Voltage multiplicand: {len(adapters_list[1]) * len(adapters_list[3])}')

        self.arrangements()