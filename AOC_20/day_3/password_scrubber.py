import os
from collections import defaultdict
from functools import reduce
from core import DefaultLogger, AOCBase

log = DefaultLogger.get_log()

class TobboganTrajectory(AOCBase):

    def __init__(self):
        self.hill = self.read_input()
        self.slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]


    def _render_hill_slope(self, x, hill_slice):
       hill_slice_render_ratio = x // hill_slice

       return hill_slice * hill_slice_render_ratio

    def move_down_slope(self):
        trees = defaultdict(int)

        for slope in self.slopes:
            x = 0
            x_slope, y_slope = slope
            hill_height = len(self.hill)

            for row in range(y_slope, hill_height, y_slope):
                x += x_slope
                hill_slice = self.hill[row].strip()
                hill_slice_render_ratio = (x // len(hill_slice)) + 1

                hill_feature = (hill_slice * hill_slice_render_ratio)[x]
                if hill_feature == '#':
                    trees[slope] += 1

        return trees

    def main(self):
        trees = self.move_down_slope()
        log.debug(f'Slope tree collisions: {trees}')

        total_multiplicand = reduce((lambda x, y: x*y), [val for _, val in trees.items()])
        log.info(f'Total tree muliplicand: {total_multiplicand}')


