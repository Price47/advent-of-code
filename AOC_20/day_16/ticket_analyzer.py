from core import DefaultLogger, AOCBase
from collections import defaultdict
import re
from functools import reduce


log = DefaultLogger.get_log()

class TicketAnalyzer(AOCBase):
    """
    https://adventofcode.com/2020/day/16

    """
    def __init__(self):
        self.data = self.read_input()
        self.valid_tickets = []
        self.valid_values = None
        self.cabin_rules = {}

    def _read_ticket(self, t):
        pass

    def _parse_rule(self, r):
        cabin, ranges = r.split(':')
        min, max = ranges.split('or')

        return cabin.strip(), min.strip(), max.strip()

    def _combine_range_values(self, ranges):
        valid_numbers = set()
        for m in ranges:
            m_lower, m_upper = m.split('-')
            for i in range(int(m_lower), int(m_upper) + 1):
                valid_numbers.add(i)

        return valid_numbers

    def quick_parse_cabin_rules(self, cabin_rules):
        valid_numbers = set()
        for r in cabin_rules:
            _, min, max = self._parse_rule(r)
            cabin_rules_set = self._combine_range_values([min, max])
            valid_numbers = {*valid_numbers, *cabin_rules_set}

        self.valid_values = valid_numbers


    def parse_cabin_rules(self, cabin_rules):
        for r in cabin_rules:
            cabin, min_range, max_range = self._parse_rule(r)
            self.cabin_rules[cabin] = self._combine_range_values([min_range, max_range])


    def organize_input(self):
        split_indices = [i for i in range(len(self.data)) if self.data[i] == '']
        cabin_rules = self.data[:split_indices[0]]
        my_ticket = self.data[split_indices[0] + 1:split_indices[1]][1]
        nearby_tickets = self.data[split_indices[1] + 1:][1:]

        return cabin_rules, my_ticket, nearby_tickets

    def sum_invalid(self, tickets):
        invalid = []
        for ticket in tickets:
            vals = [int(i) for i in ticket.split(',')]
            invalid += [v for v in vals if v not in self.valid_values]

        return sum(invalid)

    def remove_invalid(self, tickets):
        for ticket in tickets:
            ticket_vals = [int(t) for t in ticket.split(',')]
            if all([val in self.valid_values for val in ticket_vals]):
                self.valid_tickets.append(ticket_vals)


    def possible_ticket_vals(self, my_ticket):
        position_values = []
        for i in range(len(my_ticket.split(','))):
            index_vals = []
            for tic in self.valid_tickets:
                tic_position_values = set()
                for key, vals in self.cabin_rules.items():
                    if tic[i] in vals:
                        tic_position_values.add(key)
                index_vals.append(tic_position_values)

            position_values.append((i, set.intersection(*index_vals)))

        return sorted(position_values, key=lambda x: len(x[1]))

    def analyze_tickets(self, my_ticket):
        cabin_position = {}
        cabin_found = set()
        sorted_ticket_vals = self.possible_ticket_vals(my_ticket)
        for i, cabins in sorted_ticket_vals:
            cabin_set = cabins - cabin_found
            if len(cabin_set) == 1:
                cabin = cabin_set.pop()
                cabin_position[cabin] = i
                cabin_found.add(cabin)

        return cabin_position

    def main(self):
        c, m, n = self.organize_input()
        my_ticket = [int(i) for i in m.split(',')]
        self.quick_parse_cabin_rules(c)

        log.info(f'{self.sum_invalid(n)} invalid tickets')

        self.remove_invalid(n)
        self.parse_cabin_rules(c)
        self.analyze_tickets(m)

        ticket_value_positions = self.analyze_tickets(m)

        departure_vals = [t for t in ticket_value_positions if 'departure' in t]
        departure_multiplicand = reduce(
            (lambda x, y: x * y), [my_ticket[ticket_value_positions[t]] for t in departure_vals]
        )
        log.info(f'departure values is {departure_multiplicand}')

