from typing import Optional

from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()

string_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

class TrebuchetCalculator(AOCBase):
    """
    https://adventofcode.com/2023/day/1
    """
    def _check_key(self, line: str, idx: int, reverse: bool) -> Optional[int]:
        for key in string_map.keys():
            # Get string value if it exists in this index
            check_string = line[idx-len(key)+1:idx+1] if reverse else line[idx-len(key)+1:idx+1]
            if check_string == key:
                return string_map[key]

    def can_equal(self, line: str, idx: int, reverse=False, check_string_repr=True):
        if self.is_int(line[idx]):
            return line[idx]
        if check_string_repr:
            return self._check_key(line, idx, reverse)

        return None

    def parse_line(self, line: str, check_string_repr=True) -> int:
        first = None
        last = None
        line_len = len(line)

        for i in range(0, line_len):
            #iterate forward and backwards from index i to check first and last in one loop
            if not first:
                first = self.can_equal(line, i, check_string_repr=check_string_repr)
            if not last:
                last = self.can_equal(line, line_len-i-1, reverse=True, check_string_repr=check_string_repr)

            if first and last:
                # if both exist, return
                return int(f"{first}{last}")

    def calibrate(self, check_string_repr=True):
        return sum([self.parse_line(line, check_string_repr) for line in self.data])

    def run(self):
        calibration = self.calibrate(check_string_repr=False)
        log.info(f"[Calibrated Trebuchet Value] {calibration}")

        precise_calibration = self.calibrate()
        log.info(f"[Precise Calibrated Trebuchet Value] {precise_calibration}")
