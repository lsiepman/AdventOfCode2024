def read_input():
    rules = []
    pages = []
    marker = False
    with open("data/day05.txt") as file:
        for line in file:
            if line == "\n":
                marker = True
                continue
            if not marker:
                a, b = line.strip().split("|")
                rules.append((int(a), int(b)))
            else:
                pages.append([int(i) for i in line.strip().split(",")])
    return rules, pages


def create_incorrect_sets(order):
    pairs = []
    temp = order[:]
    for _ in order:
        if len(temp) > 1:
            a = temp.pop(0)
            for j in temp:
                pairs.append((j, a))
    return pairs


def middle_value(orders):
    middle_values = []
    for order in orders:
        idx = int((len(order) - 1) / 2)
        middle_values.append(order[idx])

    return sum(middle_values)


def collect_relevant_rules(order, rules):
    relevant = []
    for i in order:
        temp = [item for item in rules if i in item]
        for x, y in temp[:]:
            if x not in order or y not in order:
                temp.remove((x, y))

        relevant.extend(temp)

    return relevant


def find_first(rules):
    a = [i[0] for i in rules]
    b = [i[1] for i in rules]

    return (set(a) - set(b)).pop()


def fix_order(order, rules, new_order=[]):
    relevant_rules = collect_relevant_rules(order, rules)

    if len(order) > 1:
        first = find_first(relevant_rules)
        new_order.append(first)
        order.remove(first)

    elif len(order) == 1:
        new_order.append(order.pop())

    return new_order


def part1(rules, pages):
    correct_page_orders = []
    for order in pages:
        incorrect_pairs_for_order = create_incorrect_sets(order)
        if not set(incorrect_pairs_for_order) & set(rules):
            correct_page_orders.append(order)

    print(f"Part 1: {middle_value(correct_page_orders)}")


def part2(rules, pages):
    incorrect_page_orders = []
    for order in pages:
        incorrect_pairs_for_order = create_incorrect_sets(order)
        if set(incorrect_pairs_for_order) & set(rules):
            incorrect_page_orders.append(order)

    fixed_orders = []
    for item in incorrect_page_orders:
        new_order = []
        for _ in item[:]:
            new_order = fix_order(item, rules, new_order)

        fixed_orders.append(new_order)

    print(f"Part 2: {middle_value(fixed_orders)}")


if __name__ == "__main__":
    page_order_rules, pages_to_produce = read_input()
    part1(page_order_rules, pages_to_produce)
    part2(page_order_rules, pages_to_produce)
