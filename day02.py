def read_input():
    data = []
    with open("data/day02.txt") as file:
        for line in file:
            items = line.split()

            data.append([int(i) for i in items])

        return data


def increase(report):
    return all(i < j for i, j in zip(report, report[1:]))


def decrease(report):
    return all(i > j for i, j in zip(report, report[1:]))


def safe_diff(report):
    for idx, _ in enumerate(report[:-1]):
        if abs(report[idx] - report[idx + 1]) not in (1, 2, 3):
            return False

    return True


def problem_dampener(report):
    new_reports = []
    for idx, _ in enumerate(report):
        temp_report = report[:]
        temp_report.pop(idx)
        new_reports.append(temp_report)

    return new_reports


def part1(data):
    safe_cnt = 0
    second_chance = []
    for report in data:
        if increase(report) or decrease(report):
            if safe_diff(report):
                safe_cnt += 1
            else:
                second_chance.append(report)
        else:
            second_chance.append(report)

    print(f"Part 1: {safe_cnt}")

    return second_chance, safe_cnt


def part2(second_chance, safe_cnt):
    altered_reports = []
    for report in second_chance:
        altered_reports.append(problem_dampener(report))

    for report_group in altered_reports:
        for report in report_group:
            if increase(report) or decrease(report):
                if safe_diff(report):
                    safe_cnt += 1
                    break

    print(f"Part 2: {safe_cnt}")


if __name__ == "__main__":
    data = read_input()
    sec_chan, safe_num = part1(data)
    part2(sec_chan, safe_num)
