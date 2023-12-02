from collections import defaultdict
from functools import reduce
from typing import Dict

from core import DefaultLogger, AOCBase, AOCStr as astr


log = DefaultLogger().get_log()
COLOR_MAX_MAP = Dict[astr, defaultdict[str, int]]

class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()

    def minimum_cubes_required(self, game_cube_color_max_map: COLOR_MAX_MAP):
        total_cubes = {"blue": 14, "red": 12, "green": 13}

        sum_count = 0
        for game_num, results in game_cube_color_max_map.items():
            if all([results[color] <= total_cubes[color] for color in total_cubes.keys()]):
                sum_count += int(game_num.strip_split(" ")[-1])

        return sum_count

    def cube_power(self, game_cube_color_max_map: COLOR_MAX_MAP):
        return sum( [
            reduce(lambda x, y: x * y, results.values())
            for results in game_cube_color_max_map.values()
        ])

    def compare_cube_pulls(self, cube_pulls: str) -> defaultdict[str, int]:
        game_count = defaultdict(int)
        cube_pull_sets = cube_pulls.split(";")

        # for cube_colors in cube_pull_sets:
        cube_color_counts = [
            [astr(color_counts).strip_split(" ") for color_counts in cube_set.split(",")]
            for cube_set in cube_pull_sets
        ]

        for cube_color_count in cube_color_counts:
            for count, color in cube_color_count:
                if int(count) > game_count[color]:
                    game_count[color] = int(count)

        return game_count

    def parse_input_data(self) -> COLOR_MAX_MAP:
        game_cube_color_max_map = {}

        for line in self.data:
            game_number, cube_pulls = line.split(":")
            game_count = self.compare_cube_pulls(cube_pulls)
            game_cube_color_max_map[astr(game_number)] = game_count

        return game_cube_color_max_map


    def run(self):
        game_cube_color_max_map = self.parse_input_data()
        sum_count = self.minimum_cubes_required(game_cube_color_max_map)
        sum_power = self.cube_power(game_cube_color_max_map)

        log.info(f"[Minimum Cube Sum] {sum_count}")
        log.info(f"[Cube Power Sum] {sum_power}")