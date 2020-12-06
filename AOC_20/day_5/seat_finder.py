from core import DefaultLogger, AOCBase
import re


log = DefaultLogger.get_log()


class SeatFinder(AOCBase):
    """
    https://adventofcode.com/2020/day/5

    """

    def parse_data(self):
        operations = {
            'F': lambda x: x[:len(x) // 2],
            'B': lambda x: x[len(x) // 2:],
            'L': lambda x: x[:len(x) // 2],
            'R': lambda x: x[len(x) // 2:]
        }

        seat_results = []


        data = self.read_input()
        for d in data:
            plane_rows = list(range(128))
            plane_seats = list(range(8))
            for char in d[:7]:
                plane_rows = operations[char](plane_rows)
            for char in d[7:]:
                plane_seats = operations[char](plane_seats)

            seat = plane_seats[0]
            row = plane_rows[0]
            seat_id = (row * 8) + seat

            seat_results.append((seat_id, row, seat))

        return seat_results

    def find_seat(self, ordered_seats):
        # This shoudl really have some additional steps I think
        # but it ended up finding the right answer anyway
        missing_seat_ids = []
        seat_ids = [sid for sid, _, _ in ordered_seats]
        for x in range(len(seat_ids) - 1):
            if seat_ids[x+1] != seat_ids[x] + 1:
                missing_seat_ids.append(seat_ids[x] + 1)


        return missing_seat_ids

    def main(self):
        seat_results = self.parse_data()
        ordered_seats = sorted(seat_results, key=lambda x: x[0])

        seat = self.find_seat(ordered_seats)
        log.info(f"my seat: {seat}")


