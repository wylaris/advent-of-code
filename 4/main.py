def read_all_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    return lines

def day_one(sections):
    overlaps = 0
    for section in sections:
        elves = section.split(',')
        elf_numbs = []
        for elf in elves:
            numbs = elf.split('-')
            elf_out = []
            for i in range(int(numbs[0]), int(numbs[1]) + 1):
                elf_out.append(i)
            elf_numbs.append(elf_out)
        if (all(item in elf_numbs[0] for item in elf_numbs[1])) or (all(item in elf_numbs[1] for item in elf_numbs[0])):
            overlaps+=1
    print(overlaps)
            
def day_two(sections):
    overlaps = 0
    for section in sections:
        elves = section.split(',')
        elf_numbs = []
        for elf in elves:
            numbs = elf.split('-')
            elf_out = []
            for i in range(int(numbs[0]), int(numbs[1]) + 1):
                elf_out.append(i)
            elf_numbs.append(elf_out)
        set1 = set(elf_numbs[0])
        set2 = set(elf_numbs[1])
        intersection = list(set1 & set2)
        if len(intersection) > 0:
            overlaps += 1
    print(overlaps)

def main():
    lines = read_all_lines("in.txt")
    day_one(lines)
    day_two(lines)

if __name__ == "__main__":
    main()