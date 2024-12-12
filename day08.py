from itertools import combinations
import numpy as np


def read_input():
    data = []
    with open("data/day08.txt") as file:
        for line in file:
            data.append(list(line.strip()))

    return np.array(data)


def determine_antennas(arr):
    return [i for i in np.unique_values(arr).tolist() if i != "."]


def find_locs(arr, antenna):
    locations = np.where(arr == antenna)
    return [(i, j) for i, j in zip(locations[0], locations[1])]


def determine_pairs(loc_list):
    return [i for i in combinations(loc_list, 2)]


def calc_antinode_for_pair(loc1, loc2):
    dy = loc1[0] - loc2[0]
    dx = loc1[1] - loc2[1]

    antinode1 = (loc1[0] + dy, loc1[1] + dx)
    antinode2 = (loc2[0] - dy, loc2[1] - dx)

    return antinode1, antinode2


def harmonic_antinodes(data, loc1, loc2):
    maxY, maxX = data.shape
    antinodes = [loc1, loc2]
    dy = loc1[0] - loc2[0]
    dx = loc1[1] - loc2[1]

    for i, j in [loc1, loc2]:
        k, l = i, j
        while i > 0 and j > 0 and i < maxY and j < maxX:
            antinodes.append((i - dy, j - dx))
            i = i - dy
            j = j - dx
        while k > 0 and l > 0 and k < maxY and l < maxX:
            antinodes.append((k + dy, l + dx))
            k = k + dy
            l = l + dx

    return list(set(antinodes))


def determine_within_array(locs, arr):
    sizeY, sizeX = arr.shape
    locations = np.where(arr)
    available_locations = [(i, j) for i, j in zip(locations[0], locations[1])]

    in_array = []
    for tup in locs:
        if tup[0] >= sizeY or tup[0] < 0:
            continue
        if tup[1] >= sizeX or tup[1] < 0:
            continue
        if tup not in available_locations:
            continue

        in_array.append(tup)

    return in_array


def part1(data):
    antenna_collection = {}
    pairs = {}
    antinodes = []
    ants = determine_antennas(data)

    for i in ants:
        antenna_collection[i] = find_locs(data, i)

    for k, v in antenna_collection.items():
        pairs[k] = determine_pairs(v)

    for k, v in pairs.items():
        for i, j in v:
            antinodes.extend(calc_antinode_for_pair(i, j))

    antinodes_clean = determine_within_array(antinodes, data)

    print(f"Part 1: {len(list(set(antinodes_clean)))}")

    return pairs


def part2(data, pairs):
    antinodes = []
    for k, v in pairs.items():
        for i, j in v:
            antinodes.extend(harmonic_antinodes(data, i, j))

    antinodes_clean = determine_within_array(antinodes, data)
    print(f"Part 2: {len(list(set(antinodes_clean)))}")


if __name__ == "__main__":
    data = read_input()
    pairs = part1(data)
    part2(data, pairs)
