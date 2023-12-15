from pprint import pprint

def get_crates(filename):
    stacks = {}
    instructions = []
    with open(filename) as file:
        for line in file:
            line = line.replace('\n', '')
            if '[' in line: # Crate in line
                for i in range(0, len(line), 4):
                    letter = line[i:i+4].replace('[', '').replace(']', '').strip()
                    if letter != '':
                        stack_id = int((i/4) + 1)
                        # print(f"stack {stack_id}: {letter}")
                        if stack_id in stacks.keys():
                            stacks[stack_id].append(letter)
                        else:
                            stacks[stack_id] = [letter]
                    
            elif 'move' in line: # instruction
                instructions.append(line)
    return stacks, instructions

def extract_instruction_values(instruction):
    values = instruction.split(' ')[1::2]
    return int(values[0]), int(values[1]), int(values[2])


def day_one(crates, instructions):
    for instruction in instructions:
        count, base, dest = extract_instruction_values(instruction)
        # print(f"move {count} from {base} to {dest}")
        for i in range(0, count):
            crate = crates[base].pop(0)
            if dest in crates.keys():
                crates[dest].insert(0, crate)
            else:
                crates[dest] = [crate]
        # print(crates)
        # pprint(crates)
    out = ''
    keys = sorted(crates.keys())
    for stack in keys:
        out += crates[stack].pop(0)
    print(out)

def day_two(crates, instructions):
    for instruction in instructions:
        count, base, dest = extract_instruction_values(instruction)
        # print(f"move {count} from {base} to {dest}")
        crate = crates[base][:count]
        del crates[base][:count]
        if dest in crates.keys():
            crates[dest] = crate + crates[dest]
        else:
            crates[dest] = crate
    out = ''
    keys = sorted(crates.keys())
    for stack in keys:
        out += crates[stack][0]
    print(out)

def main():
    crates, instructions = get_crates("in.txt")
    day_one(crates, instructions)
    day_two(crates, instructions)


if __name__ == "__main__":
    main()