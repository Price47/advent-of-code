from core import DefaultLogger, AOCBase
import re


log = DefaultLogger.get_log()


class XMASEncdoingDebugger(AOCBase):
    """
    https://adventofcode.com/2020/day/9

    """
    def sum_iterator(self, data_set, check_val):
        pointer = 0
        while pointer < len(data_set) - 1:
            for i in range(pointer, len(data_set)):
                if int(data_set[pointer]) + int(data_set[i]) == int(check_val):
                    return True
            pointer += 1

        return False

    def sum_checker(self):
        preamble = 25
        data = self.read_input()
        for i in range(len(data) - preamble):
            log.debug(f'checking dataset {i}-{i + preamble}...')
            if not self.sum_iterator(data[i:i+preamble], data[i+preamble]):
                return data[i+preamble]

    def decrypt(self, target_val):
        data = [int(d) for d in self.read_input()]
        i = 0
        while i < len(data):
            segment = 1
            while i + segment < len(data):
                segment_sum = sum(data[i:i + segment])
                if segment_sum == int(target_val):
                    return data[i:i+segment]
                elif segment_sum > int(target_val):
                    break
                else:
                    segment += 1
            i += 1

    def main(self):
        invalid_number = self.sum_checker()
        log.info(f"Broken encryption point value is {invalid_number}")
        seg = self.decrypt(invalid_number)
        seg = sorted(seg)
        log.info(f'Encryption Validation segment value is {seg[0] + seg[-1]}')
