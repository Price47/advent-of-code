from core import DefaultLogger, AOCBase
from .bingo_board import Board

log = DefaultLogger().get_log()


class Bingo(AOCBase):
    def __init__(self):
        self.boards = []

    def _split(self, row):
        return list(filter(lambda c: c != '', row.split(' ')))

    def _board_generator(self, board_inputs):
        board_size = len(self._split(board_inputs[0]))
        for i in range(0, len(board_inputs) , board_size):
            self.boards.append(Board(board_inputs[i:i+5]))


    def bingo_input(self, data):
        numbers_input = data[0]
        board_inputs = list(filter(lambda r: r != '', data[2:]))
        self._board_generator(board_inputs)

        return numbers_input

    def call_number(self, n):
        unmarked_sum = None
        for b in self.boards:
            finished_board_sum = b.pick_val(n)
            if not unmarked_sum:
                unmarked_sum = finished_board_sum

        return unmarked_sum

    def find_first_winning_board(self, data):
        numbers_list = self.bingo_input(data)

        for n in numbers_list.split(','):
            if resolved_sum := self.call_number(int(n)):
                log.info(f"Winning Board id is {resolved_sum * int(n)}")
                exit()

    def last_winning_board(self, data):
        numbers_list = self.bingo_input(data)
        last_winning_board_id = 0

        for n in numbers_list.split(','):
            if resolved_sum := self.call_number(int(n)):
                last_winning_board_id = resolved_sum * int(n)

        log.info(f"Last Winning Board id is {last_winning_board_id}")

    def run(self, data=None):
        data = data or self.read_input()
        self.last_winning_board(data)
        self.find_first_winning_board(data)
