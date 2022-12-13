from functools import cmp_to_key


def input(file: str):
    return [[eval(l) for l in line.split('\n')] for line in open("day13/" + file + ".txt", "r").read().split('\n\n')]

def compare(item1: int | list, item2: int | list):
    if type(item1) == int and type(item2) == int:
        return -1 if item1 < item2 else 0 if item1 == item2 else 1
    if type(item1) == int:
        item1 = [item1]
    if type(item2) == int:
        item2 = [item2]
    
    i, j = 0, 0
    while i < len(item1) and j < len(item2):
        match compare(item1[i], item2[j]):
            case -1: return -1
            case 1: return 1
        i += 1
        j += 1
    return -1 if len(item1) < len(item2) else 0 if len(item1) == len(item2) else 1
        
def compare_all(file: str):
    return [(i, compare(*pair) == -1) for i, pair in enumerate(input(file), start=1)]

def score(file: str):
    return sum([i[0] if i[1] else 0 for i in compare_all(file)])

# Part 1
print("example 1:", score("example"))
print("part 1:", score("input"))

def sort_packets(packets: list[int | list]):
    flat_packets = []
    for pair in packets:
        flat_packets.extend(pair)
    return sorted(flat_packets, key=cmp_to_key(compare))

def insert_packets(packets: list[int | list], insert_packets = list[int | list]):
    i, j, inserted_indices, sorted_packets, sorted_insert_packets = 0, 0, [], sort_packets(packets), sort_packets(insert_packets)  
    while i < len(sorted_packets) and j < len(sorted_insert_packets):
        if compare(sorted_packets[i], sorted_insert_packets[j]) > 0:
            sorted_packets.insert(i, [sorted_insert_packets[j]])
            inserted_indices.append(i + 1)
            j += 1
        else:
            i += 1
    return inserted_indices, inserted_indices[0] * inserted_indices[1]

# Part 2
print("example 2:", insert_packets(input("example"), [[[2]], [[6]]]))
print("part 2:", insert_packets(input("input"), [[[2]], [[6]]]))