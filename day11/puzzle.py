# Common.
class Monkey:
    def __init__(self, items, operation, test, worry_level_divisor = 3):
        self.items = items
        self.operation = operation
        self.test = test
        self.worry_level_divisor = worry_level_divisor 
        self.inspect_counter = 0

    def __str__(self):
        return str.join(", ", [str(i) for i in self.items])

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        items = []
        for item in self.items:
            new_worry_level = self.operation(item) // self.worry_level_divisor
            items.append((self.test(new_worry_level), new_worry_level))
            self.inspect_counter += 1
        self.items = []
        return items

def parse_items(line: str):
    return [int(item) for item in line.removeprefix("Starting items: ").split(", ")]

def parse_operation(line: str):
    op = line.removeprefix("Operation: new = old ").split(" ")
    second_arg = lambda x : x if op[1] == "old" else int(op[1])
    match op[0]:
        case "*": return lambda x : x * second_arg(x)
        case "+": return lambda x : x + second_arg(x)

def parse_test(test: str, if_true: str, if_false: str):
    divisible_by = int(test.removeprefix("Test: divisible by "))
    monkey_if_true = int(if_true.removeprefix("If true: throw to monkey "))
    monkey_if_false = int(if_false.removeprefix("If false: throw to monkey "))
    return lambda x : monkey_if_true if (x % divisible_by == 0) else monkey_if_false

def input(file: str, worry_level_divisor = 3) -> list[Monkey]:
    monkeys, lines = [], [line.strip() for line in open("day11/" + file + ".txt", "r")]
    for l in range(0, len(lines), 7):
        monkeys.append(Monkey(parse_items(lines[l + 1]), parse_operation(lines[l + 2]), parse_test(*lines[(l + 3):(l + 6)]), worry_level_divisor))
    return monkeys

def play_round(monkeys: list[Monkey], print_debug = False):
    for i, monkey in enumerate(monkeys):
        if print_debug:
            print("Monkey", i)
        for n_monkey, item in monkey.get_items():
            monkeys[n_monkey].add_item(item)
            if print_debug:
                print(item)

def play_rounds(monkeys: list[Monkey], n_rounds = 20, print_debug = 0):
    for r in range(1, n_rounds + 1, 1):
        play_round(monkeys, print_debug=print_debug>1)
        if print_debug > 0 or r % 100 == 0:
            print("After round", r,", the monkeys are holding items with these worry levels:")
            if print_debug > 0:
                for i, monkey in enumerate(monkeys):
                    print("Monkey", i, ": ", monkey)
            for i, monkey in enumerate(monkeys):
                print("Monkey", i, "inspected items", monkey.inspect_counter, "times")
    scores = sorted([monkey.inspect_counter for monkey in monkeys])[-2:]
    return scores[0] * scores[1]

# Part 1
print("example 1:", play_rounds(input("example")))
print()
print("part 1:", play_rounds(input("input")))
print()

# Part 2
def calculate_path(file: str, n_monkey: int, item: int, n_rounds=100):
    item_tracker, monkeys = [], input(file, worry_level_divisor=1)

    for monkey in monkeys:
        monkey.get_items()
        monkey.inspect_counter = 0

    monkeys[n_monkey].add_item(item)

    for _ in range(1, n_rounds + 1, 1):
        round_tracker = []
        for monkey in monkeys:
            old_inspect_counter = monkey.inspect_counter
            for n_monkey, item in monkey.get_items():
                monkeys[n_monkey].add_item(item)
            round_tracker.append(monkey.inspect_counter - old_inspect_counter)
        item_tracker.append(tuple(round_tracker))
    
    return item_tracker

def calculate_cycles(file: str, n_rounds=500):
    item_tracker, monkeys = {}, input(file)
    for n, monkey in enumerate(monkeys):
        for item in monkey.items:
            item_tracker.update({ (n, item): calculate_path(file, n, item, n_rounds)})

    cycles = {}
    for key, items in item_tracker.items():
        unique_items = set(items)
        cycle_lengths = [items.index(u) for u in unique_items]
        cycle_length = max(cycle_lengths)
        offset = items.index(items[cycle_length + 1])
        cycles.update({ key: (offset, items[:offset], items[offset:(cycle_length+1)]) })
    
    return cycles

n_rounds = 21
monkeys = [0, 0, 0, 0]
play_rounds(input("example", worry_level_divisor=1), n_rounds=n_rounds, print_debug=1)
cycles = calculate_cycles("example")
for r in range(1, n_rounds + 1, 1):
    for key, item in cycles.items():
        offset, initial_cycle, actual_cycle = item
        index, cycle = (r - 1, initial_cycle) if r - 1 < offset else ((r - 1 - offset) % len(actual_cycle), actual_cycle)
        if r == 21 and cycle[index][2] > 0:
            print(key, cycle[index], offset, initial_cycle, actual_cycle)
        for m, c in enumerate(cycle[index]):
            monkeys[m] += c
    if r == n_rounds or r == 1 or r == 20 or r == 100 or r % 1000 == 0:
        print("== After round", r, "==")
        for m, c in enumerate(monkeys):
            print("Monkey", m, "inspected items", c, "times.")