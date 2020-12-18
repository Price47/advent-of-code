from core import DefaultLogger, AOCBase
from collections import defaultdict
import re


log = DefaultLogger.get_log()

class BitmaskDecoder(AOCBase):
    """
    https://adventofcode.com/2020/day/13

    """
    def __init__(self):
        self.data = self.read_input()
        self.mask = self._parse_mask(self.data[0])
        self.mem = self._generate_mem()

    def _parse_mask(self, m):
        return m.replace('mask =', '').strip()

    def _parse_mem(self, m):
        return int(m.strip().replace('mem[', '').replace(']', ''))

    def _generate_mem(self):
        mem_commands = []
        for c in self.data:
            if 'mem' in c:
                mem, _ = c.split('=')
                mem_commands.append(self._parse_mem(mem))

        return [list('0' * 36) for i in range(max(mem_commands) + 1)]

    def _parse_command(self, c):
        mem, val = c.split('=')
        mem = self._parse_mem(mem)
        val = list(bin(int(val.strip())).replace('0b', ''))

        return mem, val

    def mask_to_memory(self, c, m):
        for i in range(len(self.mask)-1, -1, -1):
            mask_val = self.mask[i]
            log.warning(i)
            if c:
                char = c.pop()
            else:
                char = '0'

            if mask_val == 'X':
                self.mem[m][i] = char
            else:
                self.mem[m][i] = mask_val

    def print_mem(self):
        for i, m in enumerate(self.mem):
            log.info(f'Mem {i}: {"".join(m)}')
        print()

    def sum_mem(self):
        return sum([int("".join(m), base=2) for m in self.mem])

    def main(self):
        for d in self.data:
            if 'mask' in d:
                self.mask = self._parse_mask(d)
            else:
                mem, val = self._parse_command(d)
                self.mask_to_memory(val, mem)
            log.info(self.mask)

        # self.print_mem()
        log.info(f'memory sum is {self.sum_mem()}')

