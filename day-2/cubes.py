from util import reader


def calc_is_possible_no_replace(game, num_red, num_green, num_blue):
    game = game.replace("\n", "")
    all_grabbed_cubes = game.split(";")

    total_red = 0
    total_green = 0
    total_blue = 0

    for grabbed_cubes in all_grabbed_cubes:
        cubes = grabbed_cubes.split(",")
        for cube in cubes:
            cube_parts = cube.split(" ")
            num_cubes = int(cube_parts[0] if len(cube_parts) < 2 else cube_parts[1])
            colour = cube_parts[1] if len(cube_parts) < 2 else cube_parts[2]

            if colour == "red":
                total_red += num_cubes
            if colour == "green":
                total_green += num_cubes
            if colour == "blue":
                total_blue += num_cubes

            if total_red > num_red or total_green > num_green or total_blue > num_blue:
                print(f"Line is not possible: {all_grabbed_cubes}. Red: {total_red}, Green: {total_green}, Blue: {total_blue}")
                return False

    return True


def calc_is_possible_with_replace(game, num_red, num_green, num_blue):
    game = game.replace("\n", "")
    all_grabbed_cubes = game.split(";")

    for grabbed_cubes in all_grabbed_cubes:
        total_red = 0
        total_green = 0
        total_blue = 0

        cubes = grabbed_cubes.split(",")
        for cube in cubes:
            cube_parts = cube.split(" ")
            num_cubes = int(cube_parts[0] if len(cube_parts) < 2 else cube_parts[1])
            colour = cube_parts[1] if len(cube_parts) < 2 else cube_parts[2]

            if colour == "red":
                total_red += num_cubes
            if colour == "green":
                total_green += num_cubes
            if colour == "blue":
                total_blue += num_cubes

            if total_red > num_red or total_green > num_green or total_blue > num_blue:
                print(f"Line is not possible: {all_grabbed_cubes}. Red: {total_red}, Green: {total_green}, Blue: {total_blue}")
                return False

    return True


def calc_sum_possible_games(input, num_red, num_green, num_blue, should_replace=True):
    sum = 0
    for game in input:
        game_parts = game.split(":")
        id = int(game_parts[0].split(" ")[1])
        if should_replace:
            is_possible = calc_is_possible_with_replace(game_parts[1], num_red, num_green, num_blue)
        else:
            is_possible = calc_is_possible_no_replace(game_parts[1], num_red, num_green, num_blue)
        if is_possible:
            sum += id

    return sum


if __name__ == "__main__":
    input = reader.read("resources/input.txt")
    sum_possible_games = calc_sum_possible_games(input, num_red=12, num_green=13, num_blue=14)
    assert sum_possible_games == 2317
