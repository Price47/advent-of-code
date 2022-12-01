from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):
    directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

    def __init__(self, data=None):
        self.low_points = set()
        self.basins = {}
        self.data = self._height_map(data or self.read_input())

    def _height_map(self, data):
        return [
            [int(d) for d in row] for row in data
        ]

    def _check_height(self, point, row, col, d1, d2):
        try:
            if row+d1 < 0 or col + d2 < 0:
                return True
            if point >= self.data[row + d1][col + d2]:
                return False
        except IndexError:
            return True

        return True

    def risk_level(self, point):
        row, col = point
        return self.data[row][col] + 1

    def get_height_map_risk(self):
        risk = sum([self.risk_level(point) for point in self.low_points])
        log.info(f"Risk level is {risk}")

    def get_basin_path(self, row, col, basin_size=0):
        for d1, d2 in self.directions:
            new_point = self.data[row + d1][col + d2]
            if new_point != 9 and new_point > self.data[row][col] and row+d1 > -1 and col +d2 > -1:
                print(row, col, self.data[row + d1][col + d2])

                basin_size += 1
                self.get_basin_path(row+d1, col+d2, basin_size)

        return basin_size



    def get_basins(self):
        for row, col in self.low_points:
            basin_size = self.get_basin_path(row, col)
            self.basins[row, col] = basin_size


    def run(self):
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                point = self.data[row][col]
                if all([self._check_height(point, row, col, d1, d2) for d1, d2 in self.directions]):
                    self.low_points.add((row, col))

        self.get_height_map_risk()
        self.get_basins()
        print(self.basins)




