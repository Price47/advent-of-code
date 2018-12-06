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
    time = (timestamp.hour, timestamp.minute)

    return {'date': date.strftime('%m-%d'), 'time': time, 'message': message}

def _analyze_gaurd_habbits(log):
    guard_habbits = {}
    log_index = 0
    while len(log):
        timestamp, message = log[log_index]
        if 'Guard #' in message:
            guard_number = re.findall('(?<=#)\d+', message)[0]
            for related_timestamp, related_messsage in log[log_index:]:
                log_index += 1
                if 'Guard #' in related_messsage:
                    log = log[log_index:]
                else:
                    try:
                        guard_habbits[guard_number].append(_format(related_timestamp, related_messsage))
                    except:
                        guard_habbits[guard_number] = [_format(related_timestamp, related_messsage)]
    return guard_habbits

def _group_guard_habbits(habits):
    grouped_guard_habits = {}
    for guard_number, habbits in guard_habbits.items():
        grouped_guard_habits[guard_number] = {}
        sorted_guard_habbits = sorted(habits, key=itemgetter('date'))
        grouped = groupby(sorted_guard_habbits, key=itemgetter('date'))
        for date_key, items in grouped:
            grouped_guard_habits[guard_number][date_key] = [item for item in items]

    return grouped_guard_habits

def day_4_part_1(claims):
    pass

def day_4_part_2(claims):
    pass


def main():
    print("Overlapping Fabric (in square inches): {} ".format(day_3_part_1(CLAIMS)))
    print("None overlapping claim id: {}".format(day_3_part_2(CLAIMS)))

if __name__ == '__main__':
    sorted_log = _sort_log(LOG)
    guard_habbits = _analyze_gaurd_habbits(sorted_log)
    grouped_guard_habits = _group_guard_habbits(guard_habbits)

    for guard, grouped_habbits in grouped_guard_habits.items():
        for date, grouped_habbit in grouped_habbits.items():
            print(grouped_habbit)


