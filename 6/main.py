def read_all_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    return lines

def day_one(packet, header):
    marker = []
    i = 0
    for char in packet:
        i += 1
        if char in marker:
            # print("cry")
            index = marker.index(char)
            # print(index)
            marker = marker[index + 1:]
            # print(marker)
        marker.append(char)

        if len(marker) == header:
            break
    print(i)

def main():
    lines = read_all_lines("in.txt")
    header = 4
    # header = 14
    day_one(lines[0], header)

if __name__ == "__main__":
    main()