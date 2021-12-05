from collections import defaultdict

from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class ThermalVentDetector(AOCBase):

    def __init__(self):
        self.intersections = defaultdict(int)

    def slope_diff(self, points):
        delta_x = int(points[1][0]) - int(points[0][0])
        detla_y = int(points[1][1]) - int(points[0][1])

        return delta_x, detla_y

    def read_slopes(self, data):
        slopes =[
            list((coords.split(',') for coords in d.split(' -> ')))
            for d in data
        ]

        return slopes

    def plot_horizontal(self, y, x1, x2):
        r = range(x2, x1+1) if x1 > x2 else range(x1, x2+1)
        for x in r:
            self.intersections[(x,y)] += 1

    def plot_vertical(self, x, y1, y2):
        r = range(y2, y1+1) if y1 > y2 else range(y1, y2+1)
        for y in r:
            self.intersections[(x, y)] += 1

    def plot_diagonal(self, start_coords, delta_x, delta_y):
        x = int(start_coords[0])
        y = int(start_coords[1])
        y_direction = 1 if delta_y > 0 else -1
        x_direction = 1 if delta_x > 0 else -1

        self.intersections[(x, y)] += 1
        for i in range(abs(delta_x)):
            x += x_direction
            y += y_direction
            self.intersections[(x,y)] += 1

    def intersection_points(self, slopes, handle_diag=False):
        self.intersections = defaultdict(int)
        for coords in slopes:
            delta_x, delta_y = self.slope_diff(coords)
            if delta_y == 0:
                self.plot_horizontal(int(coords[0][1]), int(coords[0][0]), int(coords[1][0]))
            elif delta_x == 0:
                self.plot_vertical(int(coords[0][0]), int(coords[0][1]), int(coords[1][1]))
            else:
                if handle_diag: self.plot_diagonal(coords[0], delta_x, delta_y)

        log.info(f"Dangerous Thermal Intersection points {(sum(1 for v in self.intersections.values() if v > 1))}")

    def run(self, data=None):
        data = data or self.read_input()
        slopes = self.read_slopes(data)
        self.intersection_points(slopes)
        self.intersection_points(slopes, True)
