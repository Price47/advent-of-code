from core import DefaultLogger, AOCBase


log = DefaultLogger().get_log()


class day(AOCBase):
    def organize_snacks(self):
        sum = 0
        sums = []

        for d in self.data:
            if d:
                sum += int(d)
            else:
                sums.append(sum)
                sum = 0

        sums.append(sum)

        return sorted(sums, reverse=True)

    def most_calories(self, sorted_calorie_counts):
        log.info(f"Highest Calorie count: {sorted_calorie_counts[0]}")

    def top_n_calories(self, sorted_calorie_counts, n=3):
        log.info(f"Top {n} Calories: {sum(sorted_calorie_counts[0:n])}")

    def run(self):
        calorie_counts = self.organize_snacks()
        self.most_calories(calorie_counts)
        self.top_n_calories(calorie_counts)
