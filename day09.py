from itertools import groupby
import time


def read_input():
    with open("data/day09.txt") as file:
        data = list(file.read().strip())
    return [int(i) for i in data]


def expand(data):
    idx_counter = 0
    expanded_data = []
    for idx, item in enumerate(data):
        if idx % 2 == 0:
            block = item * [idx_counter]
            expanded_data.extend(block)
            idx_counter += 1
        else:
            block = ["."] * item
            expanded_data.extend(block)
    return expanded_data


def compress(expanded_data):
    while "." in expanded_data:
        idx = expanded_data.index(".")
        expanded_data[idx] = expanded_data.pop(-1)
    return expanded_data


def calc_checksum(compressed_data):
    ans = 0
    for idx, value in enumerate(compressed_data):
        if value != ".":
            ans += idx * value

    return ans


def group_data(data):
    return [(k, sum(1 for i in g)) for k, g in groupby(data)]


def ungroup_data(data):
    expanded = [[i] * j for i, j in data]
    return [x for xs in expanded for x in xs]


def compress_groups(data):
    max_item = data[-1][0]
    data.append((".", 1))
    for value in range(max_item, -1, -1):
        item = [i for i in data if i[0] == value]
        idx = data.index(item[0])
        if data[idx][0] == ".":
            continue
        len_item = data[idx][1]
        available_spots = [i for i in data if i[0] == "." and i[1] >= len_item]
        if len(available_spots) == 0:
            if idx != -len(data):
                idx -= 1
                continue
        first_spot = data.index(available_spots[0])
        if first_spot > idx:
            continue
        len_spot = data[first_spot][1]
        if len_spot == len_item:
            data[first_spot] = data[idx]
            data[idx] = (".", len_item)
        else:
            data[first_spot] = (".", len_spot - len_item)
            data.insert(first_spot, data[idx])
            data[idx + 1] = (".", len_item)

        if data[idx][0] == "." or data[idx - 1] == ".":
            ungrouped = ungroup_data(data)
            data = group_data(ungrouped)

    return data


def part1(data):
    ex_data = expand(data)
    ret_data = ex_data[:]
    comp_data = compress(ex_data)
    print(f"Part 1: {calc_checksum(comp_data)}")

    return ret_data


def part2(data):
    grouped = group_data(data)
    compressed = compress_groups(grouped)
    ungrouped = ungroup_data(compressed)
    print(f"Part 2: {calc_checksum(ungrouped)}")


if __name__ == "__main__":
    data = read_input()
    expanded_data = part1(data)
    part2(expanded_data)
