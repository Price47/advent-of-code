from collections import defaultdict
from functools import reduce
from typing import List, Tuple

from core import DefaultLogger, AOCBase, AOCStr as astr


log = DefaultLogger().get_log()

dirs = {
    "up-left": (-1, -1),
    "down": (-1,0),
    "up-right": (-1,1),
    "right": (0,1),
    "left": (0,-1),
    "down-left": (1, -1),
    "up": (1,0),
    "down-right": (1,1)
}

class day(AOCBase):
    def _engine_part_number(self, row: int, col: int, part_number_sequence: astr = "") -> astr:
        try:
            if new_part_number_sequence := self.is_int(self.data[row][col+1], astr):
                part_number_sequence = self._engine_part_number(row, col+1, part_number_sequence + new_part_number_sequence)
        except IndexError:
            return part_number_sequence

        return part_number_sequence

    def get_engine_parts(self):
        engine_parts: List[Tuple[astr, Tuple[int, int]]] = []
        for row in range(len(self.data)):
            col_position = 0
            while col_position < len(self.data[row]):
                val = self.data[row][col_position]
                if part_number := self.is_int(val, astr):
                    part_number_sequence = self._engine_part_number(row, col_position, part_number)
                    engine_parts.append((part_number_sequence, (row, col_position)))
                    col_position += (len(part_number_sequence))
                else:
                    col_position += 1

        return engine_parts



    def engine_part_value(self, row, col, engine_part) -> int:
        for row_delta in range(-1, 2):
            r = min(max(row+row_delta, 0), len(self.data)-1)
            for c in range(max(col-1, 0), min(col+len(engine_part)+1, len(self.data[row]))):
                char = self.data[r][c]
                if not self.is_int(char, astr) and char != ".":
                    return int(engine_part)
                
        return 0

    def find_gear_pairs(self, row, col, engine_part):
        for row_delta in range(-1, 2):
            r = min(max(row+row_delta, 0), len(self.data)-1)
            for c in range(max(col-1, 0), min(col+len(engine_part)+1, len(self.data[row]))):
                char = self.data[r][c]
                if char == "*":
                    return r, c

    def find_part_numbers(self):
        engine_parts = self.get_engine_parts()
        engine_parts_sum = 0
        for engine_part, (row, col) in engine_parts:
            engine_parts_sum+=self.engine_part_value(row, col, engine_part)

        log.info(f"[Engine Parts Sum] {engine_parts_sum}")
        assert engine_parts_sum == 512794

    def find_gear_ratios(self):
        gear_ratio_sums = 0
        partial_gears = defaultdict(lambda: defaultdict(list))
        engine_parts = self.get_engine_parts()
        for engine_part, (row, col) in engine_parts:
            if found := self.find_gear_pairs(row, col, engine_part):
                row, col = found
                partial_gears[row][col].append(int(engine_part))

        for row_key in partial_gears:
            for col_key in partial_gears[row_key]:
                gear_parts = partial_gears[row_key][col_key]
                if len(gear_parts) == 2:
                    gear_ratio_sums += reduce(lambda x, y: x * y, gear_parts)

        assert gear_ratio_sums == 67779080
        log.info(f"[Gear Ratio Sums] {gear_ratio_sums}")

    def run(self):
        self.find_part_numbers()
        self.find_gear_ratios()













#
# from typing import List, Tuple
#
# from core import DefaultLogger, AOCBase, AOCStr as astr
#
#
# log = DefaultLogger().get_log()
#
# dirs = {
#     "up-left": (-1, -1),
#     "down": (-1,0),
#     "up-right": (-1,1),
#     "right": (0,1),
#     "left": (0,-1),
#     "down-left": (1, -1),
#     "up": (1,0),
#     "down-right": (1,1)
# }
#
# class day(AOCBase):
#
#     def check_adjacent(self, row: int, col: int):
#         adjecents = set()
#         for direction in dirs.values():
#             try:
#                 delta_row, delta_col = direction
#                 adj_val = self.data[row+delta_row][col+delta_col]
#                 if self.is_int(adj_val, astr):
#                     adjecents.add(self._engine_part_number(row+delta_row, col+delta_col, adj_val))
#             except Exception as exc:
#                 log.error(exc)
#                 log.info(f"{row+delta_row}, {col+delta_col}: {adj_val}")
#
#         return adjecents
#
#
#     def _engine_part_number(self, row: int, col: int, part_number_sequence: astr = "") -> astr:
#         # left
#         c = col
#         while c > 0:
#             c -= 1
#             if preceeding_part_number_sequence := self.is_int(self.data[row][c], astr):
#                 part_number_sequence = preceeding_part_number_sequence + part_number_sequence
#             else:
#                 break
#
#         # right
#         c = col
#         while c < len(self.data[row])-1:
#             c+=1
#             if proceeding_part_number_sequence := self.is_int(self.data[row][c], astr):
#                 part_number_sequence += proceeding_part_number_sequence
#             else:
#                 break
#
#         return part_number_sequence
#
#     def find_part_numbers(self):
#         real_ones = set()
#
#         for row in range(len(self.data)):
#             for col in range(len(self.data[row])):
#                 char = self.data[row][col]
#                 if self.is_int(char) is None and char != ".":
#                     real_ones = real_ones | self.check_adjacent(row, col)
#
#         log.warning(real_ones)
#         log.info(sum([int(engine_part) for engine_part in real_ones]))
#
#     def run(self):
#         log.info(len(self.data))
#         log.info(len(self.data[0]))
#         self.find_part_numbers()
