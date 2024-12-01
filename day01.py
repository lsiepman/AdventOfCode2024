def read_input():
    """Read data from the day01 input

    Returns:
        list1, list2:left, right list of numbers from the input
    """
    list1 = []
    list2 = []
    with open("data/day01.txt", "r") as file:
        for line in file:
            a, b = line.split("   ")
            list1.append(int(a))
            list2.append(int(b))
    return list1, list2


def calc_similarity(number: int, occurences: int):
    """calculate the increase in similarity score

    Args:
        number (int): number from one list
        occurences (int): number of occurences of number in the other list

    Returns:
        int: increase to the similarity score
    """
    return number * occurences


def part1(list1, list2):
    """Calculate the answer to part 1

    Args:
        list1 (list): One list from the input
        list2 (list): One list from the input
    """
    list1.sort()
    list2.sort()

    diff_list = []
    for i, j in zip(list1, list2):
        diff_list.append(abs(i - j))

    print(f"Part 1: {sum(diff_list)}")


def part2(list1, list2):
    """Calculate the answer to part 2

    Args:
        list1 (list): Left list from the input
        list2 (list): Right list from the input
    """
    similarity = []
    for item in list1:
        occ = list2.count(item)
        similarity.append(calc_similarity(item, occ))

    print(f"Part 2: {sum(similarity)}")


if __name__ == "__main__":
    list1, list2 = read_input()
    part1(list1, list2)
    part2(list1, list2)
