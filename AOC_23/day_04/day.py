from typing import List

from core import DefaultLogger, AOCBase, AOCStr as astr

from dataclasses import dataclass


log = DefaultLogger().get_log()


@dataclass()
class Card:
    def __init__(self, card: astr):
        card_name, card_info = card.strip_split(":")
        winning_numbers, card_numbers = astr(card_info).strip_split("|")

        self.card_no = astr(card_name).strip_split(" ")[-1]
        self.winning_numbers = [int(x) for x in astr(winning_numbers).strip_split(" ") if x]
        self.card_numbers = [int(x) for x in astr(card_numbers).strip_split(" ") if x]
        self.instances = 1

    @property
    def winning_card_numbers(self) -> List:
        return [x for x in self.card_numbers if x in self.winning_numbers]

    @property
    def winning_number_count(self) -> int:
        return len(self.winning_card_numbers)

    @property
    def card_points(self) -> int:
        val = pow(2, self.winning_number_count - 1)
        return val if val > .5 else 0

    def add_instance(self):
        self.instances += 1

    def __str__(self):
        return f"Card {self.card_no} ({self.instances})"


class day(AOCBase):

    def check_card_points(self):
        return sum([Card(card).card_points for card in self.data])

    def actual_parse_scratcher(self):
        cards = {card.card_no: card for card in [Card(card) for card in self.data]}

        for card_no, card in cards.items():
            for x in range(1, card.winning_number_count + 1):
                for _ in range(card.instances):
                    cards[astr(int(card_no) + x)].add_instance()

        return cards

    def run(self):
        card_values = self.check_card_points()
        log.info(f"Scratchers are worth {card_values} elf dollars")
        assert card_values == 23441

        cards = self.actual_parse_scratcher()
        total_cards = sum([card.instances for card in cards.values()])
        log.info(f"{total_cards} Scratchers won")
        assert total_cards == 5923918




