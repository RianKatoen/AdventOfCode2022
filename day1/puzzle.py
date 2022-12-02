def input(file):
    elves = []
    with open("day1/" + file + ".txt", "r") as input:
        calories = []
        for line in input:
            if len(line.strip()) == 0:
                elves.append(calories)
                calories = []
            else:
                calories.append(int(line))
        elves.append(calories)
    return elves
    
elves = sorted([sum(c) for c in input("example")])
print("example 1: ", elves[-1])
print("example 2: ", sum(elves[-3:]))

elves = sorted([sum(c) for c in input("input")])
print("part 1: ", elves[-1])
print("part 2: ", sum(elves[-3:]))