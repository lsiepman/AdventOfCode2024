import numpy as np


def read_input():
    data = []
    with open("data/day06.txt") as file:
        for line in file:
            data.append(list(line.strip()))

    arr = np.array(data)
    arr = np.pad(arr, 1, constant_values="&")

    return arr


def find_objects(data, object):
    if isinstance(object, list):
        loc = np.where(np.isin(data, object))
        return (loc[0].item(), loc[1].item())

    else:
        locs = np.where(data == object)
        return [(y, x) for y, x in zip(locs[0], locs[1])]


def current_direction(data):
    if np.any(data == "^"):
        return "N"
    elif np.any(data == ">"):
        return "E"
    elif np.any(data == "v"):
        return "S"
    elif np.any(data == "<"):
        return "W"
    else:
        raise ValueError("Panic!")


def move(direction, current):
    if direction == "N":
        return (current[0] - 1, current[1])
    elif direction == "E":
        return (current[0], current[1] + 1)
    elif direction == "S":
        return (current[0] + 1, current[1])
    elif direction == "W":
        return (current[0], current[1] - 1)


def check_turn_and_move(data, current, direction, obstacles):
    turn_dict = {"N": "E", "E": "S", "S": "W", "W": "N"}
    new_loc = move(direction, current)
    if new_loc in obstacles:
        return True, turn_dict[direction]
    else:
        return False, new_loc


def part1(data, guard, obstacles):

    # keep track of locations
    seen = set()
    seen.add(guard)

    # initialize values
    current = guard
    direction = current_direction(data)

    while True:
        ind, item = check_turn_and_move(data, current, direction, obstacles)
        if not ind:
            current = item
            if data[current] != "&":
                seen.add(current)
            else:
                break
        else:
            direction = item

    print(f"Part 1: {len(seen)}")
    seen.remove(guard)  # prepare for part 2

    return seen


def part2(data, route, obstacles, guard):

    cnt = 0
    for idx, loc in enumerate(route):
        new_obstacles = obstacles[:]
        new_obstacles.append(loc)

        # initialize values
        current = guard
        direction = current_direction(data)

        # keep track of locations
        seen = set()
        seen.add((direction, guard))

        while True:
            ind, item = check_turn_and_move(data, current, direction, new_obstacles)
            if not ind:
                current = item
                if data[current] != "&":
                    if (direction, current) not in seen:
                        seen.add((direction, current))
                    else:
                        cnt += 1
                        break
                else:
                    break
            else:
                direction = item

    print(f"Part 2: {cnt}")


if __name__ == "__main__":
    a = read_input()
    guard_symbols = [r"^", "v", "<", ">"]
    # find guard
    start = find_objects(a, guard_symbols)
    # find obstacles
    obst = find_objects(a, "#")

    path_guard = part1(a, start, obst)
    part2(a, path_guard, obst, start)  # 35 minutes
