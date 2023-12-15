def day_one(filename):
    with open(filename) as file:
        overall = {}
        for line in file:
            line = line.strip()
            length = int(len(line)//2)
            first = set(line[:length])
            second = set(line[length:])
            intersection = list(first & second)
            for char in intersection:
                if char.islower():
                    if char in overall:
                        overall[char] += ord(char) - 96
                    else:
                        overall[char] = ord(char) - 96
                elif char.isupper():
                    if char in overall:
                        overall[char] += ord(char) - 38
                    else:
                        overall[char] = ord(char) - 38
        print(overall)
        sum = 0
        for k,v in overall.items():
            sum += v
        print(sum)

def day_two(filename):
    lines = []
    sum = 0
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    in_all = []
    for i in range(0, len(lines), 3):
        first = set(lines[i])
        second = set(lines[i + 1])
        third = set(lines[i + 2])
        intersection = list(first & second & third)[0]
        in_all.append(intersection)
    print(in_all)
    for char in in_all:
        if char.islower():
            sum += ord(char) - 96
        else:
            sum += ord(char) - 38
    print(sum)


def main():
    # day_one("test.txt")
    day_two("in.txt")

if __name__ == "__main__":
    main()