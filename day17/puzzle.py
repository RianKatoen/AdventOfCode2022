def get_rock(n: int) -> list[list[int]]:
    match n % 5:
        case 0: return [[2, 3, 4, 5]]
        case 1: return [[3], [2, 3, 4], [3]]
        case 2: return [[2, 3, 4], [4], [4]]
        case 3: return [[2], [2], [2], [2]]
        case 4: return [[2, 3], [2, 3]]

def get_jets(file: str):
    return [c for c in open("day17/" + file + ".txt", "r").read().strip()]

def print_chamber(chamber: list[list[int]]):
    for line in chamber[::-1]:
        print_line = '|'
        for i in range(7):
            print_line += '#' if i in line else '.'
        print_line += '|'
        print(print_line)
    print('+-------+')
    print('')

def move_rock(rock: list[list[int]], chamber_part: list[list[int]], direction: str) -> list[int]:
    if direction == '>'and not(any(any([r >= 6 or r + 1 in chamber_part[i] for r in rck]) for i, rck in enumerate(rock))):
        return [[i + 1 for i in r] for r in rock]
    elif direction == '<'and not(any(any([r <= 0 or r - 1 in chamber_part[i] for r in rck]) for i, rck in enumerate(rock))):
        return [[i - 1 for i in r] for r in rock]
    else:
        return rock

def overlap(rock: list[list[int]], chamber_part: list[list[int]]):
    for r, c in zip(rock, chamber_part):
        for i in r:
            if i in c:
                return True
    return False

def play_board(file: str, n_rocks: int = 2022, determine_cycle: bool = False) -> list[list[int]]:
    n, n_jet, jets = 0, 0, get_jets(file)
    chamber: list[list[int]] = []
    cycle_height, cycles, cycle_rocks = 0, list(), list()

    while n < n_rocks or determine_cycle:
        height = len(chamber) + 3
        rock = get_rock(n)
        chamber_part = [[] for _ in rock]

        while height >= 0 and not(overlap(rock, chamber_part)):
            if n_jet % len(jets) == 0:
                n_jet = 0
                if determine_cycle:
                    if (n % 5, height - cycle_height) in cycles:
                        return n - cycle_rocks[0][0], cycle_rocks[0][0], height - cycle_rocks[0][1]
                    elif n > 5000:
                        cycle_rocks.append((n, height))
                        cycles.append((n % 5, height - cycle_height))
                    cycle_height = height

            rock = move_rock(rock, chamber_part, jets[n_jet])
            height -= 1
            n_jet += 1

            chamber_part = []
            for h in range(len(rock)):
                if 0 <= height + h < len(chamber):
                    chamber_part.append(chamber[height+h])
                else:
                    chamber_part.append([])
            
            if (n % 5) == 0 and n_jet == 0:
                return chamber

        height += 1
        n += 1

        for i, h in enumerate(range(height, height + len(rock), 1)):
            if h < len(chamber):
                chamber[h].extend(rock[i].copy())
            else:
                chamber.append(rock[i].copy())

    return chamber

# Part 1
print("example 1:", len(play_board("example", 2022)))
print("part 1:", len(play_board("input", 2022)))

def find_cycles(file: str, total_no_rocks: int = 1000000000000):
    cycle_length, cycle_start, cycle_height = play_board(file, 1000000000000, True)
    return ((total_no_rocks - cycle_start) // cycle_length) * cycle_height + len(play_board(file, cycle_start + (total_no_rocks - cycle_start) % cycle_length))

# Part 2
print("example 2:", find_cycles("example"))
print("part 2:", find_cycles("input"))