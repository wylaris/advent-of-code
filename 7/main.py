def read_all_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    return lines

def get_folder_sizes(lines):
    folder_sizes = {}
    parents = []
    for line in lines:
        if line == "**BREAK**":
            break
        if "$" in line:
            # print(f"Command: {line}")
            if "cd" in line:
                # print(parents)
                dir = line.split(" ")[-1]
                if ".." == dir:
                    parents.pop()
                    # print(parents)
                else:
                    parent = "".join(parents)
                    # print(parent, dir)
                    if parent == '/' or dir == '/':
                        current_dir = parent + dir
                    else:
                        current_dir = parent + "/" + dir
                        # print(current_dir)
                    parents.append(current_dir.replace("//", '/'))
                    # print(parents)
        elif "dir" in line:
            # print(f"Data: {line}")
            pass
        else:
            # print(f"Data: {line}")
            size = int(line.split(" ")[0])
            # print(f"File size: {size}")
            for parent in parents:
                if parent in folder_sizes.keys():
                    folder_sizes[parent] += size
                else:
                    folder_sizes[parent] = size
    return folder_sizes

def day_one(lines):
    folder_sizes = get_folder_sizes(lines)
    # print(folder_sizes)
    sum = 0
    for folder in folder_sizes.keys():
        if folder != "/":
            if folder_sizes[folder] <= 100000:
                sum += folder_sizes[folder]
    print(sum)

def day_two(lines):
    filesystem = 70000000
    update = 30000000
    folder_sizes = get_folder_sizes(lines)
    root = folder_sizes['/']
    free_space = filesystem - root
    needed = update - free_space
    print(f"Need to find: {needed}")
    this_one = update
    for folder in folder_sizes.keys():
        if folder_sizes[folder] >= needed and folder_sizes[folder] < this_one:
            this_one = folder_sizes[folder]
    print(this_one)
            

def main():
    lines = read_all_lines("in.txt")
    # day_one(lines)
    day_two(lines)

if __name__ == "__main__":
    main()