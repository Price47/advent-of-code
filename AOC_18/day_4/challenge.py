from input import LOG
import re
from datetime import datetime
from operator import itemgetter
from itertools import groupby


def _sort_log(log):
    compiled_log = [[datetime.strptime(timestamp, '%Y-%m-%d %H:%M'), message] for _, timestamp, message in [re.split("\[(.*)\]", line) for line in log]]
    sorted_log = sorted(compiled_log, key=itemgetter(0))
    return sorted_log

def _format(timestamp, message):
    date = datetime(day=timestamp.day, month=timestamp.month, year=1900)
    return {'date': date.strftime('%m-%d'), 'minute': timestamp.minute, 'message': message.strip()}

def _analyze_guard_habits(log):
    guard_habits = {}
    log_index = 0
    while log_index < len(log):
        timestamp, message = log[log_index]
        log_index += 1
        if 'Guard #' in message:
            guard_number = re.findall('(?<=#)\d+', message)[0]
            for related_timestamp, related_message in log[log_index:]:
                if 'Guard #' in related_message:
                    log = log[log_index:]
                    break
                else:
                    try:
                        guard_habits[guard_number].append(_format(related_timestamp, related_message))
                    except:
                        guard_habits[guard_number] = [_format(related_timestamp, related_message)]
    return guard_habits

def _group_guard_habits(habits):
    grouped_guard_habits = {}
    for guard_number, habits in guard_habits.items():
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
                asleep = time_group['message'] == 'falls asleep'
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

def day_4_part_1(log):
    pass

def day_4_part_2(log):
    pass


def main():
    print("Overlapping Fabric (in square inches): {} ".format(day_4_part_1(LOG)))
    print("None overlapping claim id: {}".format(day_3_part_2(CLAIMS)))

if __name__ == '__main__':
    sorted_log = _sort_log(LOG)
    guard_habits = _analyze_guard_habits(sorted_log)
    grouped_guard_habits = _group_guard_habits(guard_habits)
    guard_sleep_habits = _get_sleep_patterns(grouped_guard_habits)
    # print(guard_sleep_habits)
    guard_most_common_minutes = _most_common_minutes(guard_sleep_habits)
    sleepiest_guards = [(guard, minutes_slept) for guard, (sleep_set, minutes_slept) in guard_most_common_minutes.items()]
    sorted_sleepiest_guards = sorted(sleepiest_guards, key=itemgetter(1), reverse=True)
    sleepiest_guard, minutes_slept = sleepiest_guards[0]
    print(guard_sleep_habits[sleepiest_guard])











