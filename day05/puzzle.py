# Common.
def input(file):
    return [line for line in open("day05/" + file + ".txt", "r")]

def stacks(lines):
    stacks = []
    moves = []
    readCrates = True

    for line in lines:
        # crates are done
        if len(line.strip()) == 0 or line[1] == '1':
            readCrates = False
            continue

        # crates
        if readCrates:
            ix = 0
            while 4 * ix + 1 < len(line):
                if len(stacks) <= ix:
                    stacks.append([])
                
                crate = line[4 * ix + 1]
                if crate != ' ':
                    stacks[ix].insert(0, crate)

                ix += 1
        # moves
        elif len(line.strip()) > 0:
            split1 = line.strip("move ").split(" from ")
            split2 = split1[1].split(" to ")
            moves.append([int(split1[0]), int(split2[0]), int(split2[1])])
    
    return stacks, moves

def play_moves(stacks, moves, cratemover_9001 = False):
    for move in moves:
        from_stack = stacks[move[1] - 1]
        to_stack = stacks[move[2] - 1]
        
        # Part 2
        if cratemover_9001:
            to_stack.extend(from_stack[-move[0]:])
            del from_stack[-move[0]:]
        # Part 1
        else:
            for _ in range(move[0]):
                to_stack.append(from_stack.pop())

    return stacks

def top_crates(stacks):
    return "".join([stack[-1] for stack in stacks])

# Part 1
print("example 1: ", top_crates(play_moves(*stacks(input("example")))))
print("part 1: ", top_crates(play_moves(*stacks(input("input")))))

# Part 2
print("example 2: ", top_crates(play_moves(*stacks(input("example")), True)))
print("part 2: ", top_crates(play_moves(*stacks(input("input")), True)))