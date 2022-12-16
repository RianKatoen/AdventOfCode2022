def print_board(coords: set[tuple[tuple[int,int], tuple[int,int]]], field_of_view: set[tuple[int, int]]):
    min_x, max_x, min_y, max_y = min([min(s[0], b[0]) for s, b in coords]), max([max(s[0], b[0]) for s, b in coords]), min([min(s[1], b[1]) for s, b in coords]), max([max(s[1], b[1]) for s, b in coords])
    sensors, beacons = {sensor for sensor, _ in coords}, {beacon for _, beacon in coords}
    for y in range(min_y, max_y + 1, 1):
        line = ""
        for x in range(min_x, max_x + 1, 1):
            if (x, y) in field_of_view:
                line += "#"        
            elif (x, y) in sensors:
                line += "S"
            elif (x, y) in beacons:
                line += "B"        
            else:
                line += "."
        print(line)

def parse_coord(coord: str):
    x, y = coord.split(", ")
    return (int(x.removeprefix("x=")), int(y.removeprefix("y=")))

def input(file: str):
    lines = [line.strip().removeprefix("Sensor at ").split(": closest beacon is at ") for line in open("day15/" + file + ".txt", "r").readlines()]
    return {(parse_coord(sensor), parse_coord(beacon)) for sensor, beacon in lines}      

def distance(coord1: tuple[int,int], coord2: tuple[int,int]):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])

def in_field_of_view(sensor: tuple[int, int], beacon: tuple[int, int], coord: tuple[int,int]):
    return distance(sensor, coord) <= distance(sensor, beacon)

def in_height_of_view(sensor: tuple[int, int], beacon: tuple[int, int], height: int) -> tuple[int, int]:
    if in_field_of_view(sensor, beacon, (sensor[0], height)):
        delta = distance(sensor, beacon) - abs(sensor[1] - height)
        return (sensor[0] - delta, sensor[0] + delta)

def merge_lines(lines: list[tuple[int, int]]):
    lines = sorted(lines)
    i, j, new_lines = 0, 1, []
    while i < len(lines):
        x2 = lines[i][1]
        if not(i > 0 and x2 <= lines[i][0]):
            j = i + 1
            while j < len(lines) and x2 >= lines[j][0]:
                x2 = max(x2, lines[j][1])
                j += 1

            if i == 0 or new_lines[-1][0] >= x2: 
                new_lines.append((lines[i][0], x2))
                i = j
            elif j == len(lines):
                new_lines.append((lines[i][0], x2))
                i = len(lines)
            else:
                i += 1
        else:
            i += 1
    return new_lines

def part1(file: str, height: int):
    lines_on_height = merge_lines(filter(None, (in_height_of_view(sensor, beacon, height) for sensor, beacon in input(file))))
    no_beacons = len({beacon for _, beacon in input(file) if beacon[1] == height})
    return sum([x2 - x1 + 1 for x1, x2 in lines_on_height]) - no_beacons

# Part 1
print("example 1:", part1("example", 10))
print("part 1:", part1("input", 2000000))

def part2(file: str, size: int):
    sensors, beacons = [sensors for sensors, _ in input(file)], [beacon for _, beacon in input(file)]
    for height in range(0, size + 1, 1):
        lines_on_height = merge_lines(filter(None, (in_height_of_view(sensor, beacon, height) for sensor, beacon in zip(sensors, beacons))))
        if len(lines_on_height) > 1:
            for i in range(1, len(lines_on_height), 1):
                for x in range(lines_on_height[i-1][1] + 1, lines_on_height[i][0], 1):
                    if not((x, height) in beacons):
                        return (x, height), x * 4000000 + height

# Part 2
print("example 2:", part2("example", 20))
print("part 2:", part2("input", 4000000))