# Common.
def input(file: str):
    return [[val[0], int(val[1])] for val in [line.strip().split(" ") for line in open("day9/" + file + ".txt", "r")]]

def sign(val):
    return 1 if val >= 0 else -1

def move_head(head, move):
    match move:
        case 'L': return [head[0] - 1, head[1]]
        case 'R': return [head[0] + 1, head[1]]
        case 'U': return [head[0], head[1] + 1]
        case 'D': return [head[0], head[1] - 1]

def move_tail(tail, head):
    delta_x, delta_y = head[0] - tail[0], head[1] - tail[1]
    if abs(delta_x) > 1 and abs(delta_y) > 1:
        return [tail[0] + sign(delta_x), tail[1] + sign(delta_y)]
    elif abs(delta_x) > 1 and abs(delta_y) == 1:
        return [tail[0] + sign(delta_x), tail[1] + sign(delta_y)]
    elif abs(delta_x) == 1 and abs(delta_y) > 1:
        return [tail[0] + sign(delta_x), tail[1] + sign(delta_y)]
    elif abs(delta_x) > 1 and abs(delta_y) == 0:
        return [tail[0] + sign(delta_x), tail[1]]
    elif abs(delta_x) == 0 and abs(delta_y) > 1:
        return [tail[0], tail[1] + sign(delta_y)]
    else:
        return [tail[0], tail[1]]

def play_moves(file: str, n: int = 2):
    knots, positions = [], set()
    for i in range(n):
        knots.append([0, 0])

    for move in input(file):
        for _ in range(move[1]):
            knots[0] = move_head(knots[0], move[0])
            for i in range(n-1):
                knots[i + 1] = move_tail(knots[i + 1], knots[i])
            
            positions.add((knots[n - 1][0], knots[n - 1][1]))
    return positions

# Part 1
print("example 1:", len(play_moves("example-1")))
print("input 1:", len(play_moves("input")))

# Part 2
print("example 2:", len(play_moves("example-2", n=10)))
print("input 2:", len(play_moves("input", n=10)))