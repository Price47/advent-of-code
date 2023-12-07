import dataclasses
from typing import Dict

from core import DefaultLogger, AOCBase, AOCStr as astr


log = DefaultLogger().get_log()

MILLIMETERS = int
MILLISECONDS = int

@dataclasses.dataclass()
class Race:
    def __init__(self, time: MILLISECONDS, record: int):
        self.race_milliseconds = time
        self.record = record

    def button_duration_distance(self, milliseconds_held: MILLISECONDS) -> MILLIMETERS:
        race_duration_remaining = max(self.race_milliseconds - milliseconds_held, 0)
        return race_duration_remaining * milliseconds_held

    def winning_button_durations(self) -> int:
        return len([time for time in range(self.race_milliseconds) if self.button_duration_distance(time) > self.record])


class BoatRaces(AOCBase):
    def _parse_line(self, l: astr) -> astr:
        return astr(" ".join(astr(l.strip_split(":")[-1]).split()))

    def read_race_info(self) -> Dict[MILLISECONDS, MILLIMETERS]:
        race_durations = self._parse_line(self.data[0])
        race_records = self._parse_line(self.data[1])

        return dict(
            zip([int(x) for x in race_durations.strip_split(" ")], [int(x) for x in race_records.strip_split(" ")])
        )

    def read_race_info_with_kerning(self) -> Race:
        race_duration = int("".join(self._parse_line(self.data[0]).split()))
        race_record = int("".join(self._parse_line(self.data[1]).split()))

        return Race(race_duration, race_record)


    def run(self):
        race_info = self.read_race_info()
        margin_of_error = self.mult(
            [Race(duration, record).winning_button_durations() for duration, record in race_info.items()]
        )
        assert margin_of_error == 2374848
        log.info(f"[Margin of error] {margin_of_error}")


        race = self.read_race_info_with_kerning()
        winning_button_hold_durations = race.winning_button_durations()
        assert winning_button_hold_durations == 39132886
        log.info(f"[Winning button combinations] {winning_button_hold_durations}")

