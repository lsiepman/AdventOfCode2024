from collections import defaultdict
from itertools import product
import numexpr


def read_input():
    data = defaultdict(list)
    with open("data/day07.txt") as file:
        for line in file:
            a = line.strip()
            b, c = a.split(":")
            d = c.strip().split(" ")
            data[int(b)] = [int(i) for i in d]

    return data


def generate_options(operators, length):
    options = product(operators, repeat=length)
    return [i for i in options]


def calculate(res, options, numbers):
    if not res % numbers[-1] == 0:
        options = [i for i in options if i[-1] != "*"]
    for opts in options:
        nums = numbers[:]
        ans = nums.pop(0)
        for row, sign in zip(nums, opts):
            ans = numexpr.evaluate(f"{ans} {sign} {row}").item()
            if ans > res:
                break
        if ans == res:
            return True

    return False


def clean_numbers_and_calc(res, options, numbers):
    for opts in options:
        nums = numbers[:]
        opt2 = list(opts)
        if opt2[0] != "||":
            ans = nums.pop(0)
        else:
            ans = None

        while len(opt2) > 0:
            if opt2[0] != "||":
                ans = numexpr.evaluate(f"{ans} {opt2.pop(0)} {nums.pop(0)}").item()
            else:
                if ans is None:
                    nums[0] = int(str(nums[0]) + str(nums[1]))
                    nums.pop(1)
                    opt2.pop(0)
                    ans = nums.pop(0)
                else:
                    nums[0] = int(str(ans) + str(nums[0]))
                    opt2.pop(0)
                    ans = nums.pop(0)

            if ans > res:
                break

        if ans == res:
            return True

    return False


def check_ending(res, options, numbers):
    if not str(res).endswith(str(numbers[-1])):
        return [i for i in options if i[-1] != "||"]

    return options


def part1(data, operators=["*", "+"]):
    total = []
    for k, v in data.items():
        opts = generate_options(operators, len(v) - 1)
        works = calculate(k, opts, v)
        if works:
            total.append(k)

    print(f"Part 1: {sum(total)}")

    return total


def part2(data, correct, operators=["*", "+", "||"]):
    total = correct
    for k, v in data.items():
        if k in total:
            continue
        opts = generate_options(operators, len(v) - 1)
        opts = [i for i in opts if "||" in i]
        opts_clean = check_ending(k, opts, v)
        works = clean_numbers_and_calc(k, opts_clean, v)
        if works:
            total.append(k)

    print(f"Part 2: {sum(set(total))}")


if __name__ == "__main__":
    data = read_input()
    correct = part1(data)
    part2(data, correct)
