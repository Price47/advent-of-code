import sys
from AOC_eighteen import Challenges

if __name__ == '__main__':
    if len(sys.argv) > 1:
        day = int(sys.argv[1])
        run_challenge = Challenges.get(day)
        run_challenge()
