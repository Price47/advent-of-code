from input import BOXES


def day_2_part_1(boxes):
    check_sums = {'2_letters': 0, '3_letters': 0}
    for box in boxes:
        double = False
        triple = False
        for char in box:
            if not double and box.count(char) == 2:
                double = True
                check_sums['2_letters'] += 1
            if not triple and box.count(char) == 3:
                triple = True
                check_sums['3_letters'] += 1
            if triple and double:
                break

    return check_sums['2_letters'] * check_sums['3_letters']

def day_2_part_2(boxes):
    boxes_size = len(boxes)
    difference_index = 0
    for index, box in enumerate(boxes):
        for i in range(1, boxes_size):
            box_id_difference = 0
            box_index = index + i if index + i < boxes_size else index + i - boxes_size
            for j, char in enumerate(box):
                if char != boxes[box_index][j]:
                    box_id_difference += 1
                    difference_index = j
                if box_id_difference > 1:
                    break
            if box_id_difference < 2:
                return box[:difference_index] + box[difference_index+1:]



def main():
    print("Checksum: {}".format(day_2_part_1(BOXES)))
    print("ID like letters: {}".format(day_2_part_2(BOXES)))

if __name__ == '__main__':
    main()