import util.reader as reader

int_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def calculate_sum(lines, parse_char_words=False):
    sum = 0
    for line in lines:
        line = line.replace("\n", "")
        if parse_char_words:
            val_for_line = calc_value_for_line_with_words(line)
        else:
            val_for_line = calc_value_for_line(line)
        sum += val_for_line
        print(f"Line is: {line}. Number is: {val_for_line}, Sum is: {sum}")

    return sum


def calc_value_for_line(line):
    first = None
    second = None
    line = line.replace("\n", "")

    for char in line:
        char_as_int = to_int(char)
        if char_as_int == 0:
            continue

        if first is None:
            first = char
            second = char
        else:
            second = char

    return to_int(first + second)


def calc_value_for_line_with_words(line):
    first = None
    second = None
    line = line.replace("\n", "")

    word_search_indices = {}
    for key in int_map.keys():
        word_search_indices[key] = 0

    word = ""

    for char in line:
        char_as_int = to_int(char)

        found_word = False
        if not char_as_int:
            for curr_word, curr_word_idx in word_search_indices.items():
                char_matches = char == curr_word[curr_word_idx]
                if char_matches:
                    if curr_word_idx + 1 == len(curr_word):
                        word = curr_word
                        found_word = True
                    else:
                        word_search_indices[curr_word] = curr_word_idx + 1
                elif char == curr_word[0]:
                    word_search_indices[curr_word] = 1
                else:
                    word_search_indices[curr_word] = 0
        else:
            for word in word_search_indices:
                word_search_indices[word] = 0

        if found_word:
            char = int_map[word]

        if found_word or char_as_int:
            if first is None:
                first = char
                second = char
            else:
                second = char

    return to_int(first + second)


def to_int(str_int):
    try:
        return int(str_int)
    except ValueError:
        return 0


if __name__ == "__main__":
    sum = calculate_sum(reader.read("resources/input.txt"))
    sum_with_words = calculate_sum(reader.read("resources/input.txt"), parse_char_words=True)
    print(sum)
    print(sum_with_words)
    assert sum == 54927
    assert sum_with_words == 54477
