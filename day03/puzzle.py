# Common.
def input(file, letter_transform = lambda c : c):
    return [[letter_transform(letter) for letter in line.strip()] for line in open("day03/" + file + ".txt", "r")]

def priority(char):
    if ord(char) < 97:
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1

def sum_of_sum(entries):
    return sum([sum(entry) for entry in entries])

# Part1
def match(rucksacks):
    return [set(rucksack[0]).intersection(rucksack[1]) for rucksack in rucksacks]

def compartmentalise(rucksacks):
    results = []
    for rucksack in rucksacks:
        size = int(len(rucksack) / 2)
        results.append([rucksack[:size], rucksack[size:]])
    return results

print("example 1: ", sum_of_sum(match(compartmentalise(input("example", priority)))))
print("part 1: ", sum_of_sum(match(compartmentalise(input("input", priority)))))

# Part 2
def group(rucksacks):
    groups = []
    group = []
    for rucksack in rucksacks:
        group.append(rucksack)
        if len(group) == 3:
            groups.append(group)
            group = []
    return groups

def match(rucksacks):
    return [set(rucksack[0]).intersection(rucksack[1]).intersection(rucksack[2]) for rucksack in rucksacks]

print("example 2: ", sum_of_sum(match(group(input("example", priority)))))
print("part 2: ", sum_of_sum(match(group(input("input", priority)))))