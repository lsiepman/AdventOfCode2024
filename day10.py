import numpy as np


def read_input():
    data = []
    with open("data/day10.txt") as f:
        for line in f:
            data.append(list([int(i) for i in line.strip()]))

    return np.array(data)


def find_starts(data):
    locs = np.where(data == 0)
    return [(i, j) for i, j in zip(locs[0], locs[1])]


def find_neighbours(data, current):
    maxY, maxX = data.shape
    neigbours = {
        "up": (current[0] - 1, current[1]),
        "right": (current[0], current[1] + 1),
        "down": (current[0] + 1, current[1]),
        "left": (current[0], current[1] - 1),
    }

    for k, v in neigbours.copy().items():
        if v[0] < 0 or v[0] > maxY - 1 or v[1] < 0 or v[1] > maxX - 1:
            del neigbours[k]

    return neigbours


def increase_by_one(data, current, neighbours):
    results = []
    for i in neighbours.values():
        if data[i] == data[current] + 1:
            results.append(i)

    return results


def find_available_nines(data):
    locs = np.where(data == 9)
    return [(i, j) for i, j in zip(locs[0], locs[1])]


def walk_path(data, queue, end, part2=False):
    score = 0
    seen = set()
    while len(queue) > 0:
        current = queue.pop(0)

        if not part2:
            if current in seen:
                continue

        seen.add(current)

        if current in end:
            score += 1
            continue

        neighbours = find_neighbours(data, current)
        queue.extend(increase_by_one(data, current, neighbours))
    return score


def part1(data):
    start_locs = find_starts(data)
    ends = find_available_nines(data)
    score = 0
    for i in start_locs:
        score += walk_path(data, [i], ends)
    print(f"Part 1: {score}")


def part2(data):
    start_locs = find_starts(data)
    ends = find_available_nines(data)
    rating = 0
    for i in start_locs:
        rating += walk_path(data, [i], ends, part2=True)
    print(f"Part 2: {rating}")


if __name__ == "__main__":
    data = read_input()
    part1(data)
    part2(data)
