from util import reader

valid_symbols = "!@#$%^&*()_-+={}[]/"
search_offsets = [-1, 0, 1]


def create_matrix(engine_schematic):
    matrix = []
    for line in engine_schematic:
        line = line.replace("\n", "")
        matrix.append(list(line))
    return matrix


def sum_part_numbers(engine_matrix):
    num_start_index = -1
    num_end_index = -1

    sum_parts = 0

    for y, engine_y in enumerate(engine_matrix):
        for x, engine_x in enumerate(engine_y):
            if engine_x.isnumeric():
                if num_start_index == -1:
                    num_start_index = x
                else:
                    num_end_index = x
            else:
                sum_parts += calc_part_value(engine_matrix, num_start_index, num_end_index, y)
                num_start_index = -1
                num_end_index = -1

        sum_parts += calc_part_value(engine_matrix, num_start_index, num_end_index, y)
        num_start_index = -1
        num_end_index = -1

    return sum_parts


def within_bounds(engine_matrix, y, x):
    if 0 <= y < len(engine_matrix):
        if 0 <= x < len(engine_matrix[y]):
            return True

    return False


def is_symbol_adjacent(engine_matrix, y, x):
    for y_offset in search_offsets:
        for x_offset in search_offsets:
            curr_y = y + y_offset
            curr_x = x + x_offset

            if within_bounds(engine_matrix, curr_y, curr_x):
                val = engine_matrix[curr_y][curr_x]
                if not val.isnumeric() and not val.isalpha() and not val == ".":
                    return True

    return False


def is_adjacent(engine_matrix, start_coords, end_coords):
    adjacent = False
    start_x = start_coords[1]
    end_x = end_coords[1]

    curr_x = start_x
    while curr_x <= end_x:
        if is_symbol_adjacent(engine_matrix, start_coords[0], curr_x):
            adjacent = True
            break
        curr_x += 1

    return adjacent


def convert_to_int(engine_matrix, start_coords, end_coords):
    start_x = start_coords[1]
    end_x = end_coords[1]

    curr_x = start_x
    str_int = ""
    while curr_x <= end_x:
        str_int += engine_matrix[start_coords[0]][curr_x]
        curr_x += 1

    return int(str_int)


def calc_part_value(engine_matrix, num_start_index, num_end_index, y):
    part_value = 0
    if not num_start_index == -1 and not num_end_index == -1:
        if is_adjacent(engine_matrix, [y, num_start_index], [y, num_end_index]):
            part_value = convert_to_int(engine_matrix, [y, num_start_index], [y, num_end_index])

    return part_value


if __name__ == "__main__":
    puzzle_input = reader.read("resources/input.txt")
    part_numbers = sum_part_numbers(create_matrix(puzzle_input))
    assert part_numbers == 550918
