# Common.
def prune(file: str):
    position = []
    files = {}

    for line in [line.strip() for line in open("day7/" + file + ".txt", "r")]:
        if line[0:2] == "$ ": # is a command
            if line[0:4] == "$ cd":
                if line[5:] == "/":
                    position = []
                elif line[5:] == "..": 
                    position.pop()
                else:
                    position.append(line[5:])
        elif line[0:4] != "dir ": # is a file
            info = line.split(' ')
            file = ("" if len(position) == 0 else "/" + str.join("/", position)) + "/" + info[1]
            if not(file in files):
                files.update({ file: int(info[0]) })
    
    return files

def directory_sizes(files: dict):
    dirs = {}
    for file, size in files.items():
        path = ""
        for dir in file.split("/")[:-1]:
            path += dir + "/"
            if not(path in dirs):
                dirs.update({ path: size })
            else:
                dirs[path] += size
    return dirs

example = directory_sizes(prune("example"))
input = directory_sizes(prune("input"))

# Part 1
print("example 1: ", sum([size for size in example.values() if size <= 100000]))
print("part 1: ", sum([size for size in input.values() if size <= 100000]))

# Part 2
print("example 2: ", min([size for size in example.values() if size >= 30000000 - (70000000 - example["/"])]))
print("part 2: ", min([size for size in input.values() if size >= 30000000 - (70000000 - input["/"])]))