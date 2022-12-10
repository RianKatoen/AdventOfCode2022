# Common.
from puzzle import play_moves

def print_board(positions: set):
    min_x, max_x, min_y, max_y = min([pos[0] for pos in positions]), max([pos[0] for pos in positions]), min([pos[1] for pos in positions]), max([pos[1] for pos in positions])
    print("size: ", (min_x, max_x), ", ", (min_y, max_y))
    for y in range(min_y - 1, max_y + 1, 1)[::-1]:
        line = ""
        for x in range(min_x - 1, max_x + 1):
            line += '#' if (x, y) in positions else '.'
        print(line)

# Part 1
print_board(play_moves("example-1"))

# Part 2
print_board(play_moves("example-2", n=10))