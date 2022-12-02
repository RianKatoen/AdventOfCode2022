from input import input

elves = sorted([sum(c) for c in input("example")])
print("example  1: ", elves[-1])
print("example  2: ", sum(elves[-3:]))

elves = sorted([sum(c) for c in input("input")])
print("exercise 1: ", elves[-1])
print("exercise 2: ", sum(elves[-3:]))