from core import DefaultLogger, AOCBase
from collections import defaultdict
import re


log = DefaultLogger.get_log()

class CoordinateHandler(AOCBase):
    """
    https://adventofcode.com/2020/day/9

    """
    def __init__(self):
        data = self.read_input()
        self.instructions = [(d[0], int(d[1:])) for d in data]
        self.heading = 90
        self.coordinates = (0, 0)
        self.headings = {
            0: 'N',
            90: 'E',
            180: 'S',
            270: 'W'
        }
        self.directions = {
            'N': self._north,
            'S': self._south,
            'E': self._east,
            'W': self._west,
            'L': self._left,
            'R': self._right,
            'F': self._forward
        }

    def _add_coordinate(self, x=0, y=0):
        cord_x, cord_y = self.coordinates
        self.coordinates = (cord_x + x, cord_y + y)

    def _north(self, y):
       self._add_coordinate(y=y)

    def _south(self, y):
        self._add_coordinate(y=-y)

    def _east(self, x):
        self._add_coordinate(x=x)

    def _west(self, x):
        self._add_coordinate(x=-x)

    def _left(self, d):
        new_heading = self.heading - d
        if new_heading < 0:
            new_heading = abs(abs(new_heading) - 360)

        self.heading = new_heading

    def _right(self, d):
        '''
        heading 270
         R: 180
         450
        :param d:
        :return:
        '''
        new_heading = self.heading + d
        if new_heading > 270:
            new_heading = new_heading - 360

        self.heading = new_heading

    def _forward(self, f):
        self.directions[self.headings[self.heading]](f)

    def manhattan(self):
        x, y = self.coordinates
        dist = abs(x) + abs(y)

        log.info(f'Manhattan distance is {dist}')

    def traverse(self):
        """
        :return:
        """


        for i, v in self.instructions:
            self.directions[i](v)

        self.manhattan()

    def main(self):
        self.traverse()

class RelativeCoordinateHandler(CoordinateHandler):

    def __init__(self):
        super(RelativeCoordinateHandler, self).__init__()
        self.waypoint = (10, 1)

    def _update_waypoint(self, x=0, y=0):
        w_x, w_y = self.waypoint
        self.waypoint = (w_x + x, w_y + y)

    def rotate(self, d, v,):
        """
        https://calcworkshop.com/transformations/rotation-rules/#:~:text=A%20rotation%20is%20an%20isometric,turn%20about%20what%20point%3F)
        :param d:
        :param v:
        :return:
        """
        w_x, w_y = self.waypoint
        if v == 180:
            self.waypoint = (-w_x, -w_y)

        if d == 'R':
            if v == 90:
                self.waypoint = (w_y, -w_x)
            if v == 270:
                self.waypoint = (-w_y, w_x)
        if d == 'L':
            if v == 90:
                self.waypoint = (-w_y, w_x)
            if v == 270:
                self.waypoint = (w_y, -w_x)

    def _north(self, y):
       self._update_waypoint(y=y)

    def _south(self, y):
        self._update_waypoint(y=-y)

    def _east(self, x):
        self._update_waypoint(x=x)

    def _west(self, x):
        self._update_waypoint(x=-x)

    def _forward(self, f):
        for i in range(f):
            w_x, w_y = self.waypoint
            self._add_coordinate(w_x, w_y)

    def _right(self, v):
        self.rotate('R', v)

    def _left(self, v):
        self.rotate('L', v)
