from itertools import permutations


def input(file: str) -> list[tuple[int, int, int]]:
    return [tuple(map(int, line.split(','))) for line in open("day18/" + file + ".txt", "r")]

def side_touching(side_1: tuple[int, int], side_2: tuple[int, int]):
    return (side_1[0] == side_2[0] and abs(side_1[1] -  side_2[1]) == 1) or (abs(side_1[0] - side_2[0]) == 1 and side_1[1] == side_2[1])

def sides_touching(cube_1: tuple[int, int, int], cube_2: tuple[int, int, int]):
    if cube_1[0] == cube_2[0]:
        return side_touching((cube_1[1], cube_1[2]), (cube_2[1], cube_2[2]))
    elif cube_1[1] == cube_2[1]:
        return side_touching((cube_1[0], cube_1[2]), (cube_2[0], cube_2[2]))
    elif cube_1[2] == cube_2[2]:
        return side_touching((cube_1[0], cube_1[1]), (cube_2[0], cube_2[1]))
    return False

def no_touching_sides(cubes: list[tuple[int, int, int]]):
    n = 0
    for i, cube_1 in enumerate(cubes):
        for cube_2 in cubes[(i + 1):]:
            if sides_touching(cube_1, cube_2):
                n += 1
    return 6 * len(cubes) - 2 * n, 2 * n

# Part 1
print("example 1:", no_touching_sides(input("example"))[0])
print("part 1:", no_touching_sides(input("input"))[0])

def min_max(cubes: list[int, int, int], dim: int):
    return min([cube[dim] for cube in cubes]), max([cube[dim] for cube in cubes])

def add_point(point: tuple[int, int, int], add: tuple[int, int, int]):
    return tuple((point[0] + add[0], point[1] + add[1], point[2] + add[2]))

def simulate_water(cubes: list[tuple[int, int, int]]):
    min_x, max_x, min_y, max_y, min_z, max_z = *min_max(cubes, 0), *min_max(cubes, 1), *min_max(cubes, 2)
    all_water, new_water = set(), set()
    all_water.add((min_x - 1, min_y - 1, min_z - 1))
    new_water.add((min_x - 1, min_y - 1, min_z - 1))
    
    while len(new_water) > 0:
        all_water.update(new_water)
        new_new_water = new_water
        new_water = set()
        for water in new_new_water.copy():
            if min_x <= water[0] and not(add_point(water, (-1, 0, 0)) in all_water) and not(add_point(water, (-1, 0, 0)) in cubes):
                new_water.add(add_point(water, (-1, 0, 0)))
            if max_x >= water[0] and not(add_point(water, (1, 0, 0)) in all_water) and not(add_point(water, (1, 0, 0)) in cubes):
                new_water.add(add_point(water, (1, 0, 0)))
            if min_y <= water[1] and not(add_point(water, (0, -1, 0)) in all_water) and not(add_point(water, (0, -1, 0)) in cubes):
                new_water.add(add_point(water, (0, -1, 0)))
            if max_y >= water[1] and not(add_point(water, (0, 1, 0)) in all_water) and not(add_point(water, (0, 1, 0)) in cubes):
                new_water.add(add_point(water, (0, 1, 0)))
            if min_z <= water[2] and not(add_point(water, (0, 0, -1)) in all_water) and not(add_point(water, (0, 0, -1)) in cubes):
                new_water.add(add_point(water, (0, 0, -1)))
            if max_z >= water[2] and not(add_point(water, (0, 0, 1)) in all_water) and not(add_point(water, (0, 0, 1)) in cubes):
                new_water.add(add_point(water, (0, 0, 1)))
    
    return all_water

def no_touching_sides(cubes: list[tuple[int, int, int]], other_cubes : list[tuple[int, int, int]]):
    n = 0
    for cube_1 in cubes:
        for cube_2 in other_cubes:
            if sides_touching(cube_1, cube_2):
                n += 1
    return 6 * len(cubes) - n, n

print("example 2:", no_touching_sides(simulate_water(input("example")), input("example"))[1])
print("part 2:", no_touching_sides(simulate_water(input("input")), input("input"))[1])
