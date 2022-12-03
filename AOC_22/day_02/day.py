from core import DefaultLogger, AOCBase

log = DefaultLogger().get_log()

score_map = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3
}

class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()
        self.score_map = {
            # Rock / Rock
            "A X": score_map["X"] + 3,
            # Rock / Paper
            "A Y": score_map["Y"] + 6,
            # Rock / Scissor
            "A Z": score_map["Z"] + 0,
            # Paper / Rock
            "B X": score_map["X"] + 0,
            # Paper / Paper
            "B Y": score_map["Y"] + 3,
            # Paper / Scissors
            "B Z": score_map["Z"] + 6,
            # Scissors / Rock
            "C X": score_map["X"] + 6,
            # Scissors / Paper
            "C Y": score_map["Y"] + 0,
            # Scissors / Scissors
            "C Z": score_map["Z"] + 3
        }

    def cheat_sheet(self):
        total_score = 0
        for d in self.data:
            total_score += self.score_map[d.strip()]

        log.info(f"Total RPS Score after cheating: {total_score}")


    def determine_throw(self):
        score_fns = {
            "X": lambda x: score_map[{"A": "C", "B": "A", "C": "B"}[x]],
            "Y": lambda x: score_map[x] + 3,
            "Z": lambda x: score_map[{"A": "B", "B": "C", "C": "A"}[x]] + 6,
        }
        total_score = 0
        for d in self.data:
            opponents_throw, outcome = d.strip().split(" ")
            total_score += score_fns[outcome](opponents_throw)

        log.info(f"Total RPS Score after mildly cheating {total_score}")

    def run(self):
       self.cheat_sheet()
       self.determine_throw()