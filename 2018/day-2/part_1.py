PUZZLE_FILEPATH = 'input.txt'


def get_letters(string):
    return ''.join(set(string))


def find_counts(string, letters, n):
    for letter in letters:
        if string.count(letter) == n:
            return 1
    return 0


with open(PUZZLE_FILEPATH) as puzzle_file:
    boxes_with_two_repeats = 0
    boxes_with_three_repeats = 0

    for box_id in puzzle_file:
        letters = get_letters(box_id)
        boxes_with_two_repeats += find_counts(box_id, letters, 2)
        boxes_with_three_repeats += find_counts(box_id, letters, 3)

    print(boxes_with_two_repeats * boxes_with_three_repeats)
