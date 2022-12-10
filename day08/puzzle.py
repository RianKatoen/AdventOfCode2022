# Common.
def input(file: str):
    return [[int(char) for char in line.strip()] for line in open("day08/" + file + ".txt", "r")]

def add_tree(trees: list[(int, int)], tree):
    if not(tree in trees):
        trees.append(tree)

def visible_trees_in_line(grid: list[int]):
    i, max_height, trees = 1, grid[0], [0]
    while i < len(grid):
        if grid[i] > max_height:
            trees.append(i)
        max_height = max(max_height, grid[i])
        i += 1
    return trees

def visible_trees(grid: list[list[int]]):
    n, m = len(grid), len(grid[0])
    trees = []
    for i in range(n):
        row = grid[i]
        for tree in visible_trees_in_line(row):
            add_tree(trees, (i + 1, tree + 1))
        for tree in visible_trees_in_line(row[::-1]):
            add_tree(trees, (i + 1, m - tree))
    for j in range(m):
        col = [grid[i][j] for i in range(n)]
        for tree in visible_trees_in_line(col):
            add_tree(trees, (tree + 1, j + 1))
        for tree in visible_trees_in_line(col[::-1]):
            add_tree(trees, (n - tree, j + 1))
    return trees

# Part 1
print("example 1: ", len(visible_trees(input("example"))))
print("part 1: ", len(visible_trees(input("input"))))

# Part 2
def visible_trees_in_line(grid: list[int], tree: int):
    if len(grid) == 0:
        return []

    i, trees = 0, []
    while i < len(grid):
        if grid[i] <= tree:
            trees.append(grid[i])

        if grid[i] == tree or grid[i] > tree:
            i += len(grid)
        i += 1
    return trees

def visible_trees(grid: list[list[int]]):
    n, m = len(grid), len(grid[0])
    tree = (-1, -1)
    max_score = -1
    for i in range(n):
        row = grid[i]
        for j in range(m):
            col = [grid[r][j] for r in range(n)]

            right = visible_trees_in_line(row[(j+1):], grid[i][j]) if j < m - 1 else []
            left = visible_trees_in_line(row[(j-1)::-1] , grid[i][j]) if j > 0 else []
            up = visible_trees_in_line(col[(i-1)::-1], grid[i][j]) if i > 0 else []
            down = visible_trees_in_line(col[(i+1):], grid[i][j]) if i < n - 1 else []

            if right != None and left != None and up != None and down != None:
                score = len(right) * len(left) * len(up) * len(down)
                if score > max_score:
                    max_score = score
                    tree = (i + 1, j + 1)
    return tree, max_score

# Part 2
print("example 2: ", visible_trees(input("example")))
print("part 2: ", visible_trees(input("input")))