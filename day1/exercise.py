from input import input

elves = sorted(map(lambda c : sum(c), input("example")), reverse=True)
print("example  1: ", elves[0])
print("example  2: ", sum(elves[0:3]))

elves = sorted(map(lambda c : sum(c), input("input")), reverse=True)
print("exercise 1: ", elves[0])
print("exercise 2: ", sum(elves[0:3]))