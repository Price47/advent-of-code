from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()
        self.chunk_ends = {
            '}': '{',
            ']': '[',
            '>': '<',
            ')': '('
        }
        self.corrupted_points = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        self.incomplete_points = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
        }

        self.open_chars = self.chunk_ends.values()
        self.close_chars = self.chunk_ends.keys()

    def _line_incomplete(self, line):
        if all([c in self.open_chars for c in line]):
            return [self.incomplete_points[c] for c in line[::-1]]


    def _line_corrupted(self, line):
        char_stack = []

        for char in line:
            if len(char_stack) and self.chunk_ends.get(char) == char_stack[-1]:
                char_stack.pop()
            else:
                char_stack.append(char)

        return char_stack

    def analyze_line(self, line):
        char_stack = self._line_corrupted(line)
        if incomplete_points := self._line_incomplete(char_stack):
            incomplete_score = 0
            for p in incomplete_points:
                incomplete_score = (incomplete_score * 5) + p
            return 0, incomplete_score
        elif len(char_stack):
            for c in char_stack:
                if c in self.close_chars:
                    return self.corrupted_points[c], 0
        else:
            return 0, 0


    def run(self):
        incomplete_scores = []
        corrupt_score = 0
        for line in self.data:
            corrupted_points, incomplete_points = self.analyze_line(line)
            corrupt_score += corrupted_points
            if incomplete_points > 0:
                incomplete_scores.append(incomplete_points)

        print(sorted(incomplete_scores))
        print(sorted(incomplete_scores)[len(incomplete_scores)//2])

        log.info(f"Corrupt Score {corrupt_score}")
        log.info(f"Incomplete Score {sorted(incomplete_scores)[len(incomplete_scores)//2]}")



