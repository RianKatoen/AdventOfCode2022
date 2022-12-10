# Common.
def input(file):
    return [line.strip() for line in open("day06/" + file + ".txt", "r")]

def marker(message, n = 4):
    i = n
    while i < len(message):
        if len(message[(i - n):i]) == len(set(message[(i - n):i])):
            return i
        else:
            i += 1

example = input("example")

for i in range(4):
    print("example 1." + str(i+1) + ": ", marker(example[i]))

print("part 1: ", marker(input("input")[0]))

for i in range(4):
    print("example 2." + str(i+1) + ": ", marker(example[i], 14))

print("part 2: ", marker(input("input")[0], 14))