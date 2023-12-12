def calculate_sum(lines):
    sum = 0
    for line in lines:
        first = None
        second = None
        line = line.replace("\n", "")

        for char in line:
            int_char = to_int(char)
            if int_char == 0:
                continue

            if first is None:
                first = char
                second = char
            else:
                second = char

        char_num = first + second
        sum += to_int(char_num)
        print(f"Line is: {line}. Number is: {char_num}, Sum is: {sum}")

    return sum


def to_int(str_int):
    try:
        return int(str_int)
    except ValueError:
        return 0


if __name__ == "__main__":
    with open("./resources/input.txt", "r") as input_file:
        lines = input_file.readlines()

    print(calculate_sum(lines))
