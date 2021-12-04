from typing import List
import re

class Board:

    def __init__(self, board_input):
        self.grid = self._generate_grid(board_input)
        self.shape = (len(self.grid[0]), len(self.grid))
        self.board_resolved = False

    def _generate_grid(self, b):
        grid = []
        for r in b:
            grid.append([(c, False) for c in filter(lambda c: c!='' , r.split(' '))])

        return grid

    def row_bingo(self):
        for row in self.grid:
            if all(r[1] for r in row):
                return True

        return False

    def col_bingo(self):
        for i in range(self.shape[1]):
            if all(r[i][1] for r in self.grid):
                return True

        return False

    def check_bingo(self):
        return self.row_bingo() or self.col_bingo()

    def pick_val(self, val):
        if not self.board_resolved:
            for ix, x in enumerate(self.grid):
                for iy, y in enumerate(x):
                    if int(y[0].strip()) == int(val):
                        self.grid[ix][iy] = (y[0], True)

                    if self.check_bingo():
                        self.board_resolved = True
                        return self.sum_umarked()

    def sum_umarked(self):
        unmarked = []
        for row in self.grid:
            unmarked.extend([int(i[0]) for i in row if not i[1]])

        return sum(unmarked)

    def __repr__(self):
        str_rep = '\n'.join([' '.join([f'{c[0]}{"+" if c[1] else ""}' for c in r]) for r in self.grid])
        return f'{str_rep}\n'