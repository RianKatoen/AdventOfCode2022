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
#print("example 1:", no_touching_sides(input("example")))
#print("part 1:", no_touching_sides(input("input")))

def min_max(cubes: list[int, int, int], dim: int):
    return min([cube[dim] for cube in cubes]), max([cube[dim] for cube in cubes])

    # for cube in cubes:
    #     x_y, z = (cube[0], cube[1]), cube[2]
    #     if x_y in lines.keys():
    #         lines[x_y].append(z)
    #     else:
    #         lines[x_y] = [z]

def translate_point(point: tuple[int, int, int], dim: tuple[int, int, int]):
    new_point = [0, 0, 0]
    for i, d in enumerate(dim):
        new_point[d] = point[i]
    return tuple(new_point)

def get_external(cubes: list[tuple[int, int, int]]):
    internal_cubes = list()
    external_cubes = set()
    for dim in permutations((0, 1, 2)):
        total_min_c3, total_max_c3 = min_max(cubes, dim[2])
        lines: dict[tuple[int, int], list[int]] = {}
        for cube in cubes:
            c1_c2, c3 = (cube[dim[0]], cube[dim[1]]), cube[dim[2]]
            if c1_c2 in lines.keys():
                lines[c1_c2].append(c3)
            else:
                lines[c1_c2] = [c3]
        
        lines = {c1_c2: (min(c3), max(c3)) for c1_c2, c3 in lines.items()}
        new_cubes = []
        for c1_c2, min_max_c3 in lines.items():
            c1, c2, min_c3, max_c3 = *c1_c2, *min_max_c3
            for c3 in range(total_min_c3, total_max_c3 + 1):
                if c3 < min_c3 or c3 > max_c3:
                    new_cubes.append(translate_point((c1, c2, c3), dim))
        
        external_cubes = external_cubes.union(new_cubes)

    min_x, max_x, min_y, max_y, min_z, max_z = *min_max(cubes, 0), *min_max(cubes, 1), *min_max(cubes, 2)
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            for z in range(min_z, max_z):
                if not((x, y, z) in external_cubes):
                    internal_cubes.append((x, y, z))
                    
    print(cubes)
    print(list(set(internal_cubes)))
    return list(set(internal_cubes))

print(no_touching_sides(get_external(input("example"))))
#print(get_external(input("input")))
