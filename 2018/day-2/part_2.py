import itertools

PUZZLE_FILEPATH = 'input.txt'

ids = [box_id.strip() for box_id in open(PUZZLE_FILEPATH)]


def find_shared_characters(string_1, string_2):
    different_character = ''.join(set(string_1) - set(string_2))
    shared_characters = string_1.replace(different_character, '')
    return shared_characters


def shared_characters_of_distance_one(string_1, string_2):
    number_of_differences = sum(
        int(character_1 != character_2)
        for character_1, character_2 in zip(string_1, string_2)
    )

    if number_of_differences > 1 or number_of_differences == 0:
        return False

    return string_1, string_2


for id_1, id_2 in itertools.combinations(ids, r=2):
    output = shared_characters_of_distance_one(id_1, id_2)
    if output:
        print(find_shared_characters(*output))
