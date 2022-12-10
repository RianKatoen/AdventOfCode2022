# Common.
def chain(start, *funcs):
    res = start
    for func in funcs:
        res = [func(el) for el in res]
    return res

def input(file):
    return [line.strip() for line in open("day04/" + file + ".txt", "r")]

def split_pairs(line):
    return line.split(',')

def split_sections(pair):
    return chain(pair, lambda section : [int(id) for id in section.split('-')])

def complete_overlap(pair):
    return (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1])

# Part 1
print("example 1: ", sum(chain(input("example"), split_pairs, split_sections, complete_overlap)))
print("part 1 : ", sum(chain(input("input"), split_pairs, split_sections, complete_overlap)))

# Part 2
def overlap(pair):
    return (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0])

print("example 2: ", sum(chain(input("example"), split_pairs, split_sections, overlap)))
print("part 2: ", sum(chain(input("input"), split_pairs, split_sections, overlap)))