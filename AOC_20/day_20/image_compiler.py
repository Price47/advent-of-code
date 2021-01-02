from core import DefaultLogger, AOCBase
from .tile import Tile
from .arrangement import Arrangement
from math import sqrt

log = DefaultLogger.get_log()

class ImageComplier(AOCBase):
    """
    https://adventofcode.com/2020/day/20

    """
    def __init__(self):
        self.data = self.read_input()
        self.tiles = []
        self.arrangement = None

    def get_tiles(self):
        all_tiles = self.data
        last_index = 0
        for i in self.split_indices(all_tiles):
            self.tiles.append(Tile(all_tiles[last_index:i]))
            last_index = i + 1
        self.tiles.append(Tile(all_tiles[last_index:]))

        self.arrangement = Arrangement(sqrt(len(self.tiles)))

    def main(self):
        self.get_tiles()



