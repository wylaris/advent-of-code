def get_lists(filename):
    left = []
    right = []
    with open(filename) as file:
        for line in file:
            l = line.split("   ")
            left.append(int(l[0]))
            right.append(int(l[1]))
    return sorted(left), sorted(right)

def sum_diffs(left, right):
    diffs = 0
    for i in range(len(left)):
        diffs += abs(left[i] - right[i])
    return diffs

def sum_nums(left, right):
    sim_score = 0
    for numb in left:
        sim_score += numb * right.count(numb)
    return sim_score

def main():
    left, right = get_lists("in.txt")
    diffs = sum_diffs(left, right)
    print(diffs)
    sim_score = sum_nums(left,right)
    print(sim_score)


if __name__ == "__main__":
    main()