# Common.
def input(file: str):
    return [line.strip().split(" ") for line in open("day10/" + file + ".txt", "r")]

def get_cycles(file: str):
    x, registers = 1, [1]
    for instr in input(file):
        registers.append(x)
        if instr[0] == "addx":
            registers.append(x)
            x += int(instr[1])
    registers.append(x)
    return registers

def total_signal_strength(clocks: list[int], file: str):
    cycles = get_cycles(file)
    return [clock * cycles[clock] for clock in clocks]

# Part 1
print("example 1: ", sum(total_signal_strength(range(20, 221, 40), "example-2")))
print("part 1: ", sum(total_signal_strength(range(20, 221, 40), "input")))

# Part 2
def scan_lines(registers: list[int], rows = 6, cols = 40):
    print()
    for y in range(rows):
        line = ""
        for x in range(cols):
            line += '#' if x - 1 <= registers[x + y * 40 + 1] <= x + 1 else '.'
        print(line)

scan_lines(get_cycles("example-2"))
scan_lines(get_cycles("input"))