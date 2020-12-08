from core import DefaultLogger, AOCBase
import re


log = DefaultLogger.get_log()


class BagChecker(AOCBase):
    """
    https://adventofcode.com/2020/day/6

    """
    def organize_input(self):
        data = self.read_input()
        baggage_rules = {}
        bag_keys = set()
        for d in data:
            bag_rule = d.replace('bags', '').replace('bag', '').replace('.', '').split('contain')
            contents = bag_rule[1].split(',')
            content_keys = {}
            for c in contents:
                key = (' '.join(c.strip().split(' ')[1:])).strip()
                try:
                    content_keys[key] = int(c.strip().split(' ')[0])
                    bag_keys.add(key)
                except ValueError:
                    content_keys = 0

            bag_key = bag_rule[0].strip()
            bag_keys.add(bag_key)
            baggage_rules[bag_key] = content_keys

        return baggage_rules, bag_keys

    def get_bag_values(self, bag_color='shiny gold'):
        contained_bag_keys = {bag_color}
        target_keys_unchanged = False
        baggage_rules, bag_keys = self.organize_input()

        while not target_keys_unchanged:
            target_keys = []
            target_keys_start = len(contained_bag_keys)
            for key in bag_keys:
                baggage_rule_set = baggage_rules.get(key)
                if baggage_rule_set:
                    for k in contained_bag_keys:
                        if k in baggage_rule_set:
                            target_keys.append(key)

                for t in target_keys:
                    contained_bag_keys.add(t)

            if len(contained_bag_keys) == target_keys_start:
                target_keys_unchanged = True

        contained_bag_keys.remove(bag_color)
        return contained_bag_keys

    def _count_bag_items(self, dict_vals, top_level_bag_color='shiny gold'):
        bag_count = 0
        if isinstance(dict_vals[top_level_bag_color], dict):
            for key, val in dict_vals[top_level_bag_color].items():
                bag_count += val + (val * self._count_bag_items(dict_vals, key))
        else:
            return dict_vals[top_level_bag_color]

        return bag_count



    def bag_count(self, top_level_bag_color='shiny gold'):
        bag_count = 0
        data, _ = self.organize_input()
        for key, val in data[top_level_bag_color].items():
            bag_count += val + (val * self._count_bag_items(data, key))

        return bag_count



    def main(self):
        target_bag = 'shiny gold'
        log.info(f'{len(self.get_bag_values(target_bag))} Bags can contain {target_bag} bag')
        log.info(f'{self.bag_count(target_bag)} bags contained within {target_bag}')


