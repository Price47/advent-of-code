import dataclasses
from collections import defaultdict
from typing import List, Optional

from core import DefaultLogger, AOCBase, AOCStr as astr


log = DefaultLogger().get_log()


def numbers_in_range(start, range):
    return (start, start+range-1)

@dataclasses.dataclass()
class InfoMap:
    def __init__(self, use_sliding_ranges=False):
        self.use_sliding_ranges = use_sliding_ranges
        self.static_ranges = []
        self.sliding_ranges = []

    @property
    def ranges(self):
        return self.sliding_ranges if self.use_sliding_ranges else self.static_ranges

    def set_map_ranges(self, info: Optional[astr]):
        if info:
            if self.use_sliding_ranges:
                self.set_sliding_map_ranges(info)
            else:
                self.set_static_map_ranges(info)

    def set_static_map_ranges(self, info: Optional[astr]):
        if info:
            dest_range_start, src_range_start, range_length = info.strip_split(" ")
            self.static_ranges.append((int(dest_range_start), int(src_range_start), int(range_length)))

    def set_sliding_map_ranges(self, info: Optional[astr]):
        if info:
            info_vals = info.strip_split(" ")

            dest_range_start = int(info_vals[0])
            src_range_start = int(info_vals[1])
            range_length = int(info_vals[2])

            self.sliding_ranges.extend([
                (numbers_in_range(dest_range_start, range_length), numbers_in_range(src_range_start, range_length))
            ])

    def src_map(self, seed: int) -> int:
        for dest_start, src_start, range_length in self.ranges:
            if (src_start <= seed <= src_start + range_length):
                return seed + (dest_start - src_start)

        return seed

    def compare_ranges(self, seed_ranges):
        for r in seed_ranges:
            r_start, r_end = r
            for (dest, src) in self.ranges:
                log.debug(src)
                if r_start >= src[0] and r_end <= src[1]:
                    log.info("interesting")


    def slide_map_ranges(self, seed):
        # SLIDING WINDOWS:
        # Replace ranges with more ranges that reflect the new values
        self.compare_ranges(seed)


@dataclasses.dataclass()
class InfoMaps:
    maps = {}

    def __init__(self, map_data, use_sliding_ranges=False):
        self.use_sliding_ranges = use_sliding_ranges
        self.generate_maps(map_data)

    def generate_maps(self, map_data):
        key = None
        info_map = None

        for d in map_data:
            if "map" in d:
                key = d.replace(":", "").strip()
                info_map = InfoMap(self.use_sliding_ranges)
            else:
                if key and info_map:
                    info_map.set_map_ranges(d)
                    self.maps[key] = info_map

    def find_mapping(self, seed):
        val = seed
        for key in self.maps:
            info_map = self.maps[key]
            val = info_map.src_map(val)

        return val

    def do(self, seed):
        val = seed
        for key in self.maps:
            info_map = self.maps[key]
            val = info_map.slide_map_ranges(val)

        return val


class day(AOCBase):
    def parse_seeds(self):
        return [int(s) for s in astr(self.data[0].split(":")[-1]).strip_split(" ")]

    def parse_seed_ranges(self):
        seeds = self.parse_seeds()
        seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]
        a = []

        for (v, r) in seed_ranges:
            a.append(numbers_in_range(v,r))

        return a

    def find_closest_seed_locations(self):
        info_maps = InfoMaps(self.data[1:])
        seeds = self.parse_seeds()

        locs = []
        for seed in seeds:
            info_maps.find_mapping(seed)
            locs.append(info_maps.find_mapping(seed))

        min_distance = min(locs)
        log.info(f"Closest Seed to plant {min_distance}")
        assert min_distance == 35


    def find_closest_seed_range_locations(self):
        info_maps = InfoMaps(self.data[1:], use_sliding_ranges=True)
        seeds = self.parse_seed_ranges()

        # [79...92, 55...67]
        log.info(seeds)

        locs = []
        # for seed in seeds[:2]:
        info_maps.do(seeds)
            # info_maps.find_mapping(seed)
            # locs.append(info_maps.find_mapping(seed))

        # min_distance = min(locs)
        # log.info(f"Closest Seed to plant {min_distance}")
        # assert min_distance == 46

    def run(self):
        # self.find_closest_seed_locations()
        self.find_closest_seed_range_locations()

