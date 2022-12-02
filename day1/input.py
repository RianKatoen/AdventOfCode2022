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