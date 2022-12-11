# Common.
class Item:
    def __init__(self, value, base):
        self.value = value
        self.base = base
    
    def __str__(self): return self.value

    def set_value(self, value): self.value = value % self.base
    def add(self, value): self.set_value(self.value + value)
    def divide(self, value): self.set_value(self.value // value)
    def multiply(self, value): self.set_value(self.value * value)
    def square(self): self.multiply(self.value)
    def is_divisible_by(self, value): return self.value % value == 0
            
class Monkey:
    def __init__(self, items, operation, test, worry_level_divisor = 3, own_divisor = 1):
        self.items = items
        self.operation = operation
        self.test = test
        self.worry_level_divisor = worry_level_divisor
        self.own_divisor = own_divisor
        self.inspect_counter = 0

    def __str__(self): return str.join(", ", [str(i) for i in self.items])
    def add_item(self, item): self.items.append(item)

    def get_items(self):
        items = []
        for item in self.items:
            self.operation(item)
            if self.worry_level_divisor > 0:
                item.divide(self.worry_level_divisor)

            new_monkey = self.test(item)
            items.append((new_monkey, item))
            
            self.inspect_counter += 1
        self.items = []
        return items

def parse_items(line: str, base: int):
    return list([Item(int(item), base) for item in line.removeprefix("Starting items: ").split(", ")])

def parse_operation(line: str):
    op = line.removeprefix("Operation: new = old ").split(" ")
    if op[1] == "old":
        return lambda x : x.square()
    else:
        match op[0]:
            case '+': return lambda x : x.add(int(op[1]))
            case '*': return lambda x : x.multiply(int(op[1]))

def parse_test(test: str, if_true: str, if_false: str):
    divisible_by = int(test.removeprefix("Test: divisible by "))
    monkey_if_true = int(if_true.removeprefix("If true: throw to monkey "))
    monkey_if_false = int(if_false.removeprefix("If false: throw to monkey "))
    return lambda x : monkey_if_true if x.is_divisible_by(divisible_by) else monkey_if_false

def input(file: str, worry_level_divisor = 3) -> list[Monkey]:
    base, monkeys, lines = 1, [], [line.strip() for line in open("day11/" + file + ".txt", "r")]
    for l in range(0, len(lines), 7):
        base *= int(lines[l + 3].removeprefix("Test: divisible by "))
    for l in range(0, len(lines), 7):
        divisible_by = int(lines[l + 3].removeprefix("Test: divisible by "))
        if worry_level_divisor > 0:
            monkeys.append(Monkey(parse_items(lines[l + 1], base), parse_operation(lines[l + 2]), parse_test(*lines[(l + 3):(l + 6)]), worry_level_divisor, own_divisor=divisible_by))
        else:
            monkeys.append(Monkey(parse_items(lines[l + 1], base), parse_operation(lines[l + 2]), parse_test(*lines[(l + 3):(l + 6)]), worry_level_divisor=-1, own_divisor=divisible_by))
    return monkeys

def play_round(monkeys: list[Monkey]):
    for i, monkey in enumerate(monkeys):
        for n_monkey, item in monkey.get_items():
            monkeys[n_monkey].add_item(item)

def play_rounds(monkeys: list[Monkey], n_rounds = 20, print_debug = 0):
    for r in range(1, n_rounds + 1, 1):
        play_round(monkeys)
        if (print_debug == 1 and r % 1000) or (print_debug > 1):
            print("After round", r,", the monkeys are holding items with these worry levels:")
            if print_debug > 1:
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

# Part 1
print("example 2:", play_rounds(input("example", worry_level_divisor=0), n_rounds=10000))
print()
print("part 2:", play_rounds(input("input", worry_level_divisor=0), n_rounds=10000))
print()