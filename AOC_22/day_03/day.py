from core import DefaultLogger, AOCBase

log = DefaultLogger().get_log()


item_priority = {item: priority + 1 for priority, item in enumerate([
    c for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
])}


class rucksack:
    def __init__(self, content):
        compartment_size = len(content) // 2
        self.left_compartment = content[0:compartment_size]
        self.right_compartment = content[compartment_size::]

    def shared_items(self):
        return set([item for item in self.left_compartment if item in self.right_compartment])


class day(AOCBase):
    def __init__(self, data=None):
        self.data = data or self.read_input()

    def check_rucksack_compartments(self):
        item_sum = 0
        for d in self.data:
            shared_items = rucksack(d).shared_items()
            item_sum += item_priority[shared_items.pop()]

        log.info(f"Misplaced item sum is {item_sum}")

    def check_groups(self):
        badge_item_priorities = 0
        for i in range(0, len(self.data), 3):
            group = self.data[i:i+3]
            badge = set([item for item in group[0] if item in group[1] and item in group[2]])
            badge_item_priorities += item_priority[badge.pop()]

        log.info(f"Badge item priority is {badge_item_priorities}")

    def run(self):
        self.check_rucksack_compartments()
        self.check_groups()
