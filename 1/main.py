def get_top_three(filename):
    most = []
    with open(filename) as f:
        total = 0
        for line in f:
            if line == "\n":
                if len(most) < 3:
                    most.append(total)
                else:
                    if min(most) < total:
                        most = sorted(most)
                        most[0] = total
                total = 0
            else:
                total += int(line)
    return most

def part_1(top_three):
    print(f"Most calories by a single elf: {max(top_three)}")

def part_2(top_three):
    print(f"Most calories carried by three elves: {sum(top_three)}")

def main():
    top_three = get_top_three("in.txt")
    part_1(top_three)
    part_2(top_three)

if __name__ == "__main__":
    main()