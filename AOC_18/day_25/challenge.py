from input import FREQUENCIES

def day_1_part_1(frequencies):
    return sum(frequencies)

def day_2_part_2(frequencies):
    base_frequency = 0
    past_frequencies = [0]
    iteration = 0
    while True:
        print("Frequency iteration {}...".format(iteration))
        for frequency in frequencies:
            base_frequency += frequency

            if base_frequency in past_frequencies:
                print("Success! Synchronous frequency found!")
                return base_frequency
            else:
                past_frequencies.append(base_frequency)
        iteration += 1
        print("Frequency iteration {} found no synchronous frequencies".format(iteration))

def main():
    print("Resulting Frequnecy: {} ".format(day_1_part_1(FREQUENCIES)))
    print("Synchronous Frequency: {}".format(day_2_part_2(FREQUENCIES)))

if __name__ == '__main__':
    main()