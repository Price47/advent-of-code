from input import POLYMER
from operator import itemgetter


def _compareCase(a, b):
    equal = a==b
    caseEqual = a.lower() == b or a.upper() == b
    reaction = caseEqual and not equal

    return reaction

def _sequence_polymer(polymer):
    sequencing = True
    elements_removed = 0

    while sequencing:
        "elements removed: {}".format(elements_removed)
        element_was_removed = False
        for i, element in enumerate(polymer):
            if (i+1 < len(polymer)):
                if _compareCase(element, polymer[i+1]):
                    polymer = polymer[:i] + polymer[i+2:]
                    element_was_removed = True
                    break
        if not element_was_removed: sequencing = False

    return polymer

def _batch_sequence(polymer, batch_size=250):
    last_polymer_length = len(polymer)
    done = False
    iteration = 0
    while not done:
        iteration += 1
        new_polymer = ''
        polymers = [polymer[i:i + batch_size] for i in range(0, len(polymer), batch_size)]
        for chunk, polymer in enumerate(polymers):
            new_polymer += _sequence_polymer(polymer)
            print('finished sequencing iteration {}, chunk {}'.format(iteration, chunk+1))
        done = len(new_polymer) == last_polymer_length
        polymer = new_polymer
        last_polymer_length = len(new_polymer)

    polymer = _sequence_polymer(polymer)

    return polymer

def day_5_part_1(polymer):
    new_polymer = _batch_sequence(polymer)
    return len(new_polymer)

def day_5_part_2(polymer):
    reactions = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        new_polymer = "".join([element for element in polymer if element.lower() != letter.lower()])
        new_polymer = _batch_sequence(new_polymer)
        reactions[letter] = len(new_polymer)
    reactions = sorted([(letter, polymer_len) for letter, polymer_len in reactions.items()], key=itemgetter(1))

    return reactions[0]

def main():
    print("Polymer length: {} ".format(day_5_part_1(POLYMER)))
    element, length = day_5_part_2(POLYMER)
    print("Shortest Polymer: {} [removed element {}]".format(length, element))

if __name__ == '__main__':
    element, length = day_5_part_2(POLYMER)
    print("Shortest Polymer: {} [removed element {}]".format(length, element))
