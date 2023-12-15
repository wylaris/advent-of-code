def read_all_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    return lines

def determine_and_move_tail(rope, knot, positions):
    xDiff = rope[knot-1][0] - rope[knot][0]
    yDiff = rope[knot-1][1] - rope[knot][1]
    # print("Before:")
    # print(f"Prev Knot {knot-1}: {rope[knot-1]} Knot {knot}: {rope[knot]}")
    # print(f"xDiff: {xDiff} yDiff: {yDiff}")
    if abs(xDiff) > 1 or abs(yDiff) > 1:
        if abs(xDiff) > abs(yDiff):
            rope[knot][0] += xDiff - int((xDiff/abs(xDiff)))
            rope[knot][1] = rope[knot-1][1]
        elif abs(xDiff) < abs(yDiff):
            rope[knot][1] += yDiff - int((yDiff/abs(yDiff)))
            rope[knot][0] = rope[knot-1][0]
        else:
            rope[knot][0] += xDiff - int((xDiff/abs(xDiff)))
            rope[knot][1] += yDiff - int((yDiff/abs(yDiff)))
    # print("\nAfter:")
    # print(f"Prev Knot {knot-1}: {rope[knot-1]} Knot {knot}: {rope[knot]}\n")
    if rope[len(rope)-1] not in positions:
        positions.append(rope[len(rope)-1].copy())

def day_one(lines):
    rope = []
    ropeLength = 10
    for i in range(0,ropeLength):
        rope.append([0,0])
    positions = [[0,0]]
    for l in lines:
        direction = l.split()[0]
        iterations = l.split()[1]
        for i in range(0, int(iterations)):
            if direction == "R":
                rope[0][0] += 1
            if direction == "U":
                rope[0][1] += 1
            if direction == "L":
                rope[0][0] -= 1
            if direction == "D":
                rope[0][1] -= 1
            for knot in range(1,len(rope)):
                determine_and_move_tail(rope, knot, positions)
        #print(rope)
    print(f"Number of unique positions: {len(positions)}")

def day_two(lines):
    rope = []
    ropeLength = 10
    for i in range(0,ropeLength):
        rope.append([0,0])
    positions = [[0,0]]
    for l in lines:
        direction = l.split()[0]
        iterations = l.split()[1]
        for i in range(0, int(iterations)):
            if direction == "R":
                rope[0][0] += 1
            if direction == "U":
                rope[0][1] += 1
            if direction == "L":
                rope[0][0] -= 1
            if direction == "D":
                rope[0][1] -= 1
            for knot in range(1,len(rope)):
                determine_and_move_tail(rope, knot, positions)
        #print(rope)
    print(f"Number of unique positions: {len(positions)}")

def main():
    lines = read_all_lines("in.txt")
    # day_one(lines)
    day_two(lines) # 2765

if __name__ == "__main__":
    main()