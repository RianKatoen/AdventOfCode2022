def input(file: str):
    return [[tuple([int(coord) for coord in coords.split(',')]) for coords in line.strip().split(" -> ")] for line in open("day14/" + file + ".txt", "r").readlines()]

def print_board(rocks: set[tuple[int, int]], sand: set[tuple[int, int]] = set(), falling_sand: tuple[int, int] = (-1, -1)):
    coords = rocks.copy().union(sand.copy())
    if falling_sand != (-1, -1):
        coords = coords.union(set([falling_sand]))

    min_x, max_x, min_y, max_y = min([r[0] for r in coords]), max([r[0] for r in coords]), 0, max([r[1] for r in coords])
    for y in range(min_y, max_y + 1, 1):
        line = ""
        for x in range(min_x, max_x + 1, 1):
            if (x, y) == falling_sand:
                line += "+"
            elif (x, y) in sand:
                line += "o"
            elif (x, y) in rocks:
                line += "#"        
            else:
                line += "."
        print(line)

def sign(a, b):
    return 1 if a < b else 0 if a == b else -1

def create_rocks(rock_lines: list[list[tuple[int, int]]]):
    rocks = set()
    for rock_line in rock_lines:
        for point_1, point_2 in zip(rock_line[:-1], rock_line[1:]):
            x, y, sign_x, sign_y = *point_1, sign(point_1[0], point_2[0]), sign(point_1[1], point_2[1])
            while (x, y) != point_2:
                rocks.add((x, y))
                x, y = x + sign_x, y + sign_y
            rocks.add((x, y))
    return rocks

def drop_sand(file: str, delta_floor_y = -1):
    rocks, sand = create_rocks(input(file)), set()
    falling_sand, max_y = (500, 0), max([r[1] for r in rocks]) + (delta_floor_y if delta_floor_y > 0 else 0)
    while falling_sand[1] <= max_y:
        falling_sand = (500, 0)
        while falling_sand != (-1, -1) and falling_sand[1] <= max_y:
            if not((falling_sand[0], falling_sand[1] + 1) in rocks or (falling_sand[0], falling_sand[1] + 1) in sand):
                falling_sand = (falling_sand[0], falling_sand[1] + 1)
            elif not((falling_sand[0] - 1, falling_sand[1] + 1) in rocks or (falling_sand[0] - 1, falling_sand[1] + 1) in sand):
                falling_sand =  (falling_sand[0] - 1, falling_sand[1] + 1)
            elif not((falling_sand[0] + 1, falling_sand[1] + 1) in rocks or (falling_sand[0] + 1, falling_sand[1] + 1) in sand):
                falling_sand = (falling_sand[0] + 1, falling_sand[1] + 1)
            else:
                sand.add(falling_sand)
                falling_sand = (-1, -1)

        if delta_floor_y > 0:
            if (500, 0) in sand:
                break
            elif falling_sand[1] > max_y:
                rocks.add((falling_sand[0], falling_sand[1] - 1))
                sand.add((falling_sand[0], falling_sand[1] - 2))
                falling_sand = (500, 0)

    print_board(rocks, sand)

    return rocks, sand, falling_sand

# Part 1
print("example 1:", len(drop_sand("example")[1]))
print("part 1:", len(drop_sand("input")[1]))

# Part 2
print("example 2:", len(drop_sand("example", delta_floor_y=2)[1]))
print("part 2:", len(drop_sand("input", delta_floor_y=2)[1]))