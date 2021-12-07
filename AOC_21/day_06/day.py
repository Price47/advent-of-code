from core import DefaultLogger, AOCBase
from .lattern_fish import Fish


log = DefaultLogger().get_log()


class School(AOCBase):

    def __init__(self):
        self.school = []
        self.growth_simulation_days = 256

    def simulate_fish_growth(self):
        for day in range(self.growth_simulation_days):
            new_fish = 0
            for f in self.school:
                if f.age():
                    new_fish += 1

            for i in range(new_fish):
                self.school.append(Fish())

    def better_simulate_fish_growth(self, ages):
        fish = [0] * 9
        for i in ages:
            fish[int(i)] += 1

        for day in range(self.growth_simulation_days):
            new_fish = fish[0]
            for f in range(6):
                fish[f] = fish[f+1]

            fish[6] = new_fish + fish[7]
            fish[7] = fish[8]
            fish[8] = new_fish

        print(sum([f for f in fish]))


    def run(self, data=None):
        data = data or self.read_input()

        fish_ages = data[0].split(',')
        for f in fish_ages:
            self.school.append(Fish(int(f)))

        # self.simulate_fish_growth()
        self.better_simulate_fish_growth(fish_ages)
