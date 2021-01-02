from core import DefaultLogger, AOCBase
from collections import defaultdict
import re
from functools import reduce
from itertools import permutations


log = DefaultLogger.get_log()

class MessageDecoder(AOCBase):
    """
    https://adventofcode.com/2020/day/19

    """
    def __init__(self):
        self.data = self.read_input()
        self.rules = []
        self.messages = []
        self.decoded_values = {}
        self.valid_messages = []

    def _is_msg(self, m):
        return all([i in ('a', 'b', '|', ' ') for i in list(m)])

    def parse_input(self):
        split = [i for i in range(len(self.data)) if self.data[i] == ''][0]
        rules = []
        self.messages = self.data[split + 1:]

        for rule in self.data[:split]:
            i, rule_val = rule.split(':')
            rule_val = rule_val.strip().replace('"', '')

            rule_tuple = (int(i.strip()), rule_val, self._is_msg(rule_val))
            rules.append(rule_tuple)

        rules = sorted(rules, key=lambda x: x[0])
        self.rules = rules

        return rules[0]

    def decode_messages(self):
        while any(r[2] == False for r in self.rules[1:]):
            for idx, msg, _ in [r for r in self.rules if r[2]]:
                for i in range(1, len(self.rules)):
                    r = self.rules[i]
                    m = r[1].replace(str(idx), msg)

                    self.rules[i] = (r[0], m, self._is_msg(m))

        for r in self.rules[1:]:
            self.decoded_values[r[0]] = [x.strip().replace(' ', '') for x in r[1].split('|')]

    def _thread_message(self, r, msg):
        rule_val = self.decoded_values[int(r)]
        for thread in rule_val.split('|'):
            self._thread_message(r, msg)
            log.warning(msg)

    def main(self):
        check_rule = self.parse_input()
        self.decode_messages()

        log.debug(self.decoded_values)
        check_rules = check_rule[1].split(' ')
        perms = self.decoded_values[int(check_rules[0])]
        log.error(perms)
        for r in check_rules[1:]:
            perms = ([p+x for p in perms for x in self.decoded_values[int(r)]])
            log.info(perms)

