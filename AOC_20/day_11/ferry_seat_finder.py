from core import DefaultLogger, AOCBase
from collections import defaultdict
import re


log = DefaultLogger.get_log()

class FerrySeatFinder(AOCBase):
    """
    https://adventofcode.com/2020/day/11

    """

    def __init__(self):
        super(FerrySeatFinder, self).__init__()
        self.data = self.read_input()
        self.seats = [[*d] for d in self.data]
        self.shape = (len(self.seats), len(self.seats[0]))

    def _val_at(self, x, y):
        try:
            if x < 0 or y < 0:
                return
            return self.seats[y][x]
        except IndexError:
            return

    def print_seats(self, seats=None):
        s = seats if seats else self.seats
        for n in s:
            log.info(n)

        print()

    def occupied_seats(self):
        return(
            sum([
                len([char for char in row if char =='#'])
                for row in self.seats
            ])
        )

    def check_adjacent(self, x, y, seats):
        seat_val = self._val_at(x, y)
        occupied_adj = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue # this is the current seat

                adj_val = self._val_at(x+i, y+j)

                if adj_val == '#':
                    occupied_adj += 1

        if seat_val == 'L' and occupied_adj == 0:
            seat_val = '#'
        if seat_val == '#' and occupied_adj >= 4:
            seat_val = 'L'

        seats[y][x] = seat_val

    def check_seats_in_sight(self, x, y, seats):
        max_x, max_y = self.shape
        seat_val = self._val_at(x, y)

        advance_direction = {
            (-1,-1): lambda x_delta, y_delta: (x_delta-1, y_delta-1),
            (-1, 0): lambda x_delta, y_delta: (x_delta-1, y_delta),
            (-1, 1): lambda x_delta, y_delta: (x_delta-1, y_delta+1),
            (0, -1): lambda x_delta, y_delta: (x_delta, y_delta-1),
            (0, 1): lambda x_delta, y_delta: (x_delta, y_delta+1),
            (1, -1): lambda x_delta, y_delta: (x_delta+1, y_delta-1),
            (1, 0): lambda x_delta, y_delta: (x_delta+1, y_delta),
            (1, 1): lambda x_delta, y_delta: (x_delta+1, y_delta+1)
        }

        occupied_seats = []

        occupied_adj = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                s_x = x
                s_y = y
                sight_line = True
                if i == 0 and j == 0:
                    sight_line = False # this is the current seat

                while sight_line:
                    # log.info(advance_direction[(i, j)](s_x, s_y))
                    s_x, s_y = advance_direction[(i, j)](s_x, s_y)

                    if s_x < 0 or s_y < 0 or s_x >= max_x or s_y >= max_y:
                        # log.info('out of param')
                        # log.error((s_x, s_y))
                        sight_line = False
                    adj_val = self._val_at(s_x, s_y)

                    if adj_val == '#':
                        occupied_seats.append((s_x, s_y))
                        occupied_adj += 1
                        break
                    if adj_val == 'L':
                        break


        if seat_val == 'L' and occupied_adj == 0:
            seat_val = '#'
        if seat_val == '#' and occupied_adj >= 5:
            seat_val = 'L'

        seats[y][x] = seat_val

    def find_seats(self, in_sightline=False):
        check_fn = self.check_seats_in_sight if in_sightline else self.check_adjacent
        last_occupied = None
        i = 1

        while True:
            log.debug(f"Checking seat configuration {i}")
            new_seats = [[*d] for d in self.seats]
            x_range, y_range = self.shape
            for y in range(y_range):
                for x in range(x_range):
                    if self._val_at(x, y) != '.':
                        check_fn(x, y, new_seats)


            self.seats = new_seats

            occupied = self.occupied_seats()
            if occupied == last_occupied:
                log.info(f"Stablized seat config has {occupied} occupied seats")
                return

            i += 1
            last_occupied = occupied


    def main(self):
        self.find_seats(True)
