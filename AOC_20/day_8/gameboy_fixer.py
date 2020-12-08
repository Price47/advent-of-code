from core import DefaultLogger, AOCBase
import re


log = DefaultLogger.get_log()


class GameboyFixer(AOCBase):
    """
    https://adventofcode.com/2020/day/8

    """
    accumulator = 0

    def _acc(self, x):
        self.accumulator += int(x)
        return 1

    def _jmp(self, x):
        return int(x)

    def _nop(self, x):
        return 1

    def run_ops(self, data=None):
        i = 0
        self.accumulator = 0
        data = data if data else self.read_input()
        instructions_run = []

        ops = {
            'acc': self._acc,
            'jmp': self._jmp,
            'nop': self._nop
        }

        while i < len(data):
            instructions_run.append(i)
            op, val = data[i].strip().split(' ')
            i += ops[op.strip()](val.strip())
            if i in instructions_run:
                log.debug(f'accumulator value is at recursion point is {self.accumulator}')
                return -1

        return 1

    def alter_startup_code(self, alter_command, start_index):
        replace_val = {'jmp': 'nop', 'nop': 'jmp'}
        data = self.read_input()
        for i in range(start_index, len(data)):
            if alter_command in data[i]:
                data[i] = data[i].replace(alter_command, replace_val[alter_command])
                return data, i+1

        return None, None

    def run_and_alter_ops(self):
        for command in ['nop', 'jmp']:
            x = -1
            i = 0
            while x == -1:
                data, i = self.alter_startup_code(command, i)
                x = self.run_ops(data)

                if not i:
                    x = None

            if i is not None:
                log.info(self.accumulator)
                exit()

    def main(self):
        self.run_ops()
        self.run_and_alter_ops()
