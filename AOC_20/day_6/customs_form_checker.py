from core import DefaultLogger, AOCBase
import re


log = DefaultLogger.get_log()


class CustomsFormChecker(AOCBase):
    """
    https://adventofcode.com/2020/day/6

    """

    def check_common_answers(self):
        data = self.read_input()
        group_data_sets = []
        group_data = []
        for d in data:
            if not d:
                group_data_sets.append(group_data)
                group_data = []
            else:
                group_data.append([char for char in d])

        group_data_sets.append(group_data)

        return group_data_sets

    def get_common_answers_sum(self):
        sum = 0
        common_answer_groups = self.check_common_answers()

        for group in common_answer_groups:
            sum += len(set(group[0]).intersection(*group))

        return sum

    def check_answers(self):
        data = self.read_input()
        group_data_sets =[]
        group_data = set()
        for d in data:
            if not d:
                group_data_sets.append(group_data)
                group_data = set()
            else:
                for char in d:
                    group_data.add(char)

        group_data_sets.append(group_data)

        return sorted(group_data_sets, key=lambda x: len(x), reverse=True)

    def main(self):
        group_answers = self.check_answers()
        log.info(f'Sum of shared answers is {sum([len(group_answer) for group_answer in group_answers])}')
        common_answer_sums = self.get_common_answers_sum()
        log.info(f'Sum of total common answers is {common_answer_sums}')


