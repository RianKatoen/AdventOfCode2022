def to_height(c: str):
    match c:
        case 'S': return 0
        case 'E': return 27
        case _: return ord(c) - ord('a') + 1

def input(file: str):
    return [[to_height(c) for c in line.strip()] for line in open("day12/" + file + ".txt", "r")]

def find(heights: list[list[int]], search_height: int):
    for i, row in enumerate(heights):
        for j, height in enumerate(row):
            if height == search_height:
                return (i, j)

def determine_moves(heights: list[list[int]], i: int, j: int):
    current_height, height, width, new_pos = heights[i][j], len(heights), len(heights[0]), []
    if i > 0 and heights[i-1][j] - current_height <= 1:
        new_pos.append((i-1, j))
    if i < height - 1 and heights[i+1][j] - current_height <= 1:
        new_pos.append((i+1, j))
    if j > 0 and heights[i][j-1] - current_height <= 1:
        new_pos.append((i, j-1))
    if j < width - 1 and heights[i][j+1] - current_height <= 1:
        new_pos.append((i, j+1))
    return new_pos

def prune(heights: list[list[int]], i = -1, j = -1):
    start, end = find(heights, 0) if i < 0 or j < 0 else (i, j), find(heights, 27)
    counter, locations, visited = 0, set([start]), set([start])
    while not(end in visited) and len(locations) > 0:
        counter += 1
        for loc in locations.copy():
            locations.discard(loc)
            for move in determine_moves(heights, *loc):
                if not(move in visited):
                    locations.add(move)
                    visited.add(move)
    return counter if end in visited else -1

def prune_start(file: str):
    heights = input(file)
    height, width, answers = len(heights), len(heights[0]), []
    for i in range(height):
        for j in range(width):
            if heights[i][j] == 0 or heights[i][j] == 1:
                answer = prune(heights, i, j)
                if answer >= 0:
                    answers.append(answer)
    return min(answers)

# Part 1
print("example 1:", prune(input("example-1")))
print("part 1:", prune(input("input")))

# Part 2
print("example 1:", prune_start("example-1"))
print("part 1:", prune_start("input"))