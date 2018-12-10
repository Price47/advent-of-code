from input import LOG
import re
from datetime import datetime
from operator import itemgetter
from itertools import groupby


def _sort_log(log):
    compiled_log = [[datetime.strptime(timestamp, '%Y-%m-%d %H:%M'), message] for _, timestamp, message in [re.split("\[(.*)\]", line) for line in log]]
    sorted_log = sorted(compiled_log, key=itemgetter(0))
    return sorted_log

def _format(entry):
    message = re.split(r'(\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\])', entry)[1:]
    date = datetime.strptime(message[0], '[%Y-%m-%d %H:%M:%f]')
    date = date.replace(year=1900)
    return {'date': date.strftime('%m-%d'), 'minute': date.minute, 'message': message[1].strip()}

def _analyze_guard_habits(log):
    guard_habits = {}
    log = "|".join(["[{}] {}".format(timestamp, message) for timestamp, message in log])
    log_lines = re.split(r'\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\]\s*Guard',log)[1:]
    for line in log_lines:
        guard_data = line.split("|")
        guard_number = re.findall('(?<=#)\d+', guard_data[0])[0]
        for entry in guard_data[1:]:
            if entry:
                try:
                    guard_habits[guard_number].append(_format(entry))
                except:
                    guard_habits[guard_number] = [_format(entry)]

    return guard_habits

def _group_guard_habits(habits):
    grouped_guard_habits = {}
    for guard_number, habits in habits.items():
        grouped_guard_habits[guard_number] = {}
        sorted_guard_habits = sorted(habits, key=itemgetter('date'))
        grouped = groupby(sorted_guard_habits, key=itemgetter('date'))
        for date_key, items in grouped:
            grouped_guard_habits[guard_number][date_key] = [item for item in items]

    return grouped_guard_habits

def _get_sleep_patterns(grouped_guard_habits):
    guards_sleep_pattern = {}
    for guard, grouped_habits in grouped_guard_habits.items():
        guards_sleep_pattern[guard] = {}
        for date, grouped_habit in grouped_habits.items():
            time_sorted_grouped_habit = sorted(grouped_habit, key=itemgetter('minute'))
            minutes_asleep = {}
            last_index = 0
            for time_group in time_sorted_grouped_habit:
                asleep = time_group['message'] != 'falls asleep'
                minute = time_group['minute']
                time_group_minutes = {i: asleep for i in range(last_index, minute)}
                minutes_asleep.update(time_group_minutes)
                last_index = minute
            minutes_asleep.update({i: False for i in range(last_index, 60)})
            for i in range(time_sorted_grouped_habit[0]['minute']):
                minutes_asleep[i] = False
            minutes_asleep.update({i: False for i in range(time_sorted_grouped_habit[0]['minute'])})
            guards_sleep_pattern[guard][date] = minutes_asleep

    return guards_sleep_pattern

def _most_common_minutes(guard_sleep_habits):
    guard_waking_minutes = {}
    for guard, sleep_patterns in guard_sleep_habits.items():
        guard_waking_minutes[guard] = []
        for date, sleep_pattern in sleep_patterns.items():
            waking_minutes = set([minute for minute, asleep in sleep_pattern.items() if asleep])
            guard_waking_minutes[guard].append(waking_minutes)
    guard_most_common_minutes = {}
    for guard, sets in guard_waking_minutes.items():
        minutes_slept = 0
        common_minutes = None
        for sleep_set in sets:
            minutes_slept += len(sleep_set)
            if not common_minutes:
                common_minutes = sleep_set
            else:
                common_minutes = common_minutes & sleep_set
        guard_most_common_minutes[guard] = (common_minutes, minutes_slept)
    return guard_most_common_minutes

def _get_most_common_minute(sorted_sleepiest_guard, guard_sleep_habits):
    sleepiest_guard, minutes_slept = sorted_sleepiest_guard
    minutes_asleep = [
        set([minute for minute, asleep in minutes.items() if asleep])
        for date, minutes in guard_sleep_habits[sleepiest_guard].items()
        ]

    minute_count = {i: 0 for i in range(60)}

    for minutes_asleep_set in minutes_asleep:
        for minute in minutes_asleep_set:
            minute_count[minute] += 1

    return [(minute, count) for minute, count in minute_count.items()]

def calculate_times():
    sorted_log = _sort_log(LOG)
    guard_habits = _analyze_guard_habits(sorted_log)
    grouped_guard_habits = _group_guard_habits(guard_habits)
    guard_sleep_habits = _get_sleep_patterns(grouped_guard_habits)
    guard_most_common_minutes = _most_common_minutes(guard_sleep_habits)
    sleepiest_guards = [(guard, minutes_slept) for guard, (sleep_set, minutes_slept) in
                        guard_most_common_minutes.items()]
    sorted_sleepiest_guards = sorted(sleepiest_guards, key=itemgetter(1), reverse=True)

    return sorted_sleepiest_guards, guard_sleep_habits

def day_4_part_1(log):
    sorted_sleepiest_guards, guard_sleep_habits = calculate_times()

    like_minutes = _get_most_common_minute(sorted_sleepiest_guards[0], guard_sleep_habits)
    sorted_like_minutes = sorted(like_minutes, key=itemgetter(1), reverse=True)

    sleepiest_guard = sorted_sleepiest_guards[0][0]
    most_slept_minute = sorted_like_minutes[0][0]
    total = int(sleepiest_guard) * int(most_slept_minute)

    return sleepiest_guard, most_slept_minute, total

def day_4_part_2(log):
    sorted_sleepiest_guards, guard_sleep_habits = calculate_times()

    like_minutes = {}
    for guard in sorted_sleepiest_guards:
        like_minutes[guard[0]] = sorted(_get_most_common_minute(guard, guard_sleep_habits),
                                        key=itemgetter(1),
                                        reverse=True)[0]
    sorted_most_frequently_sleepy_guard = sorted(
        [(guard, minute, count) for guard, (minute, count) in like_minutes.items()],
        key=itemgetter(2),
        reverse=True
    )

    return sorted_most_frequently_sleepy_guard[0]


def main():
    sleepiest_guard, most_slept_minute, total = day_4_part_1(LOG)
    print("Gaurd {} is most asleep at minute {} ({})".format(sleepiest_guard, most_slept_minute, total))
    frequently_sleepy_guard, minute_asleep, times_asleep = day_4_part_2(LOG)
    print("Guard {} most frequently asleep at {} ({} times) [answer: {}]"
          .format(frequently_sleepy_guard, minute_asleep,
                  times_asleep,
                  (int(frequently_sleepy_guard) * int(minute_asleep)))
          )

if __name__ == '__main__':
    main()











