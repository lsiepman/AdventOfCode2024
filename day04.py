import numpy as np


def read_input():
    data = []
    with open("data/day04.txt") as file:
        for line in file:
            data.append(list(line.strip()))

    return np.array(data)


def find_xmas(a, loc_X, loc_Y):
    xmas_count = 0
    # horizontal, XMAS
    try:
        if (
            a[loc_X, loc_Y]
            + a[loc_X + 1, loc_Y]
            + a[loc_X + 2, loc_Y]
            + a[loc_X + 3, loc_Y]
            == "XMAS"
        ):
            xmas_count += 1
    except IndexError:
        pass

    # diagonal, XMAS
    try:
        if (
            a[loc_X, loc_Y]
            + a[loc_X + 1, loc_Y + 1]
            + a[loc_X + 2, loc_Y + 2]
            + a[loc_X + 3, loc_Y + 3]
            == "XMAS"
        ):
            xmas_count += 1
    except IndexError:
        pass

    return xmas_count


def find_x_mas(a, loc_X, loc_Y):
    mas_count = 0

    # prevent negative indexing
    if loc_X == 0 or loc_Y == 0:
        return mas_count

    try:
        if a[loc_X - 1, loc_Y - 1] + a[loc_X, loc_Y] + a[loc_X + 1, loc_Y + 1] in (
            "MAS",
            "SAM",
        ) and a[loc_X - 1, loc_Y + 1] + a[loc_X, loc_Y] + a[loc_X + 1, loc_Y - 1] in (
            "MAS",
            "SAM",
        ):
            mas_count += 1

    except IndexError:
        pass

    return mas_count


def part1(a):
    answer = 0
    for rotation in range(4):
        temp_arr = np.rot90(a, rotation)
        locations = np.where(temp_arr == "X")
        for i, j in zip(locations[0], locations[1]):
            answer += find_xmas(temp_arr, i, j)

    print(f"Part 1: {answer}")


def part2(a):
    answer = 0
    locations = np.where(a == "A")

    for i, j in zip(locations[0], locations[1]):
        answer += find_x_mas(a, i, j)

    print(f"Part 2: {answer}")


if __name__ == "__main__":
    arr = read_input()
    part1(arr)
    part2(arr)
