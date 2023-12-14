def calculate_sum(lines):
    sum = 0
    for line in lines:
        line = line.replace("\n", "")
        val_for_line = value_for_line(line)
        sum += val_for_line
        print(f"Line is: {line}. Number is: {val_for_line}, Sum is: {sum}")

    return sum


def value_for_line(line):
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

    return to_int(first + second)


def to_int(str_int):
    try:
        return int(str_int)
    except ValueError:
        return 0


if __name__ == "__main__":
    with open("./resources/input.txt", "r") as input_file:
        lines = input_file.readlines()

    sum = calculate_sum(lines)
    print(sum)
    assert sum == 54927
