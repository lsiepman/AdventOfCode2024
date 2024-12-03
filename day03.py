import re


def read_input():
    with open("data/day03.txt") as file:
        mem = file.read()
        return mem


def find_pieces(line):
    return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)


def multiply(instructions):
    return int(instructions[0]) * int(instructions[1])


def part1(inp):
    correct_data = find_pieces(inp)
    answer = 0
    for i in correct_data:
        answer += multiply(i)

    print(f"Part 1: {answer}")


def part2(inp):
    segmented = re.split(r"(do(n't)?\(\))", inp)
    fragments = []
    set_to_on = True
    for i in segmented:
        if set_to_on:
            if i == "don't()":
                set_to_on = False
                continue
            else:
                if i is not None:
                    fragments.extend(find_pieces(i))
                else:
                    continue
        elif i == "do()":
            set_to_on = True

    answer = 0
    for i in fragments:
        answer += multiply(i)
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    data = read_input()
    part1(data)
    part2(data)
