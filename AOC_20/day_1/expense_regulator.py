import os
from functools import reduce
from core import DefaultLogger


log = DefaultLogger().get_log()


class expenseRegulator:
    """
    resolve expense accounts
    """
    def __init__(self, sum_val=2020, expenses=None):
        self.expenses = expenses
        self.sum_components = []
        self.sum_val = sum_val
        self.expenses_size = 0
        self.expenses_resolved = False

    def _read_expenses(self):
        log.info('getting vals')
        if not self.expenses:
            with open(f'{os.getcwd()}/day_1/input.txt') as f:
                content = f.read()
                self.expenses = [int(s) for s in content.splitlines()]
                log.info(self.expenses)

        self.expenses_size = len(self.expenses)

    def find_sums_recursive(self, depth=2, pointer_index=0, current_depth=0):
        """
        Recursively cycle through list and check sum of values
        
        :param depth:
        :param pointer_index:
        :param current_depth:
        :return:
        """
        while pointer_index < self.expenses_size and not self.expenses_resolved:
            log.debug(f'pointer at depth {current_depth} is {pointer_index}')
            depth_pointer = pointer_index

            if current_depth < depth-1:
                self.sum_components.append(self.expenses[depth_pointer])
                self.find_sums_recursive(depth, depth_pointer + 1, current_depth + 1)
            else:
                for i in range(depth_pointer, self.expenses_size):
                    log.debug(f'index {i} at depth {current_depth}')
                    if sum(self.sum_components) + self.expenses[i] == self.sum_val:
                        self.sum_components.append(self.expenses[i])
                        self.expenses_resolved = True
                        break
                break

            if not self.expenses_resolved: self.sum_components.pop(-1)
            pointer_index += 1


    def resolve_accounts_recursive(self, n=3):
        """
        Find n number of values that combine to equal self.sum_total in a list

        :param n: int, values to combine
        :return: int, values multiplied together
        """
        self._read_expenses()
        self.find_sums_recursive(n)

        if self.sum_components:
            log.info(self.sum_components)
            multiplicand = reduce((lambda x,y: x*y), self.sum_components)
            log.info(multiplicand)

            return multiplicand
        else:
            log.error("Couldn't find sums")
