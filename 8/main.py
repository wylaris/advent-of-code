def read_all_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    return lines

def build_matrix(lines):
    matrix = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        matrix.append(row)
    return matrix

def check_tree_blocked(matrix, row_i, col_j):
    visible_trees = 0
    tree = matrix[row_i][col_j]
    # print(tree)
    north_visible = True
    east_visible = True
    south_visible = True
    west_visible = True

    # north
    for i in range(0, row_i):
        north_tree = matrix[i][col_j]
        if north_tree >= tree:
            north_visible = False

    # east
    for j in range(col_j + 1, len(matrix[0])):
        east_tree = matrix[row_i][j]
        if east_tree >= tree:
            east_visible = False

    # south
    for i in range(row_i + 1, len(matrix)):
        south_tree = matrix[i][col_j]
        if south_tree >= tree:
            south_visible = False

    # west
    for j in range(0, col_j ):
        west_tree = matrix[row_i][j]
        if west_tree >= tree:
            west_visible = False

    # print(tree, north_visible, east_visible, south_visible, west_visible)
    if not north_visible and not east_visible and not south_visible and not west_visible:
        # print("not visible")
        pass
    else:
        # print("visible")
        visible_trees += 1
    return visible_trees

def day_one(matrix):
    row_max = len(matrix) -1
    col_max = len(matrix[0]) -1
    row_i = 0
    visible_trees = 0

    for row in matrix:
        if row_i == 0 or row_i == row_max:
            visible_trees += len(row)
            row_i += 1
            continue
        col_j = 0
        for col in row:
            if col_j == 0 or col_j == col_max:
                visible_trees += 1
                col_j += 1
                continue
            visible_trees += check_tree_blocked(matrix, row_i, col_j)

            col_j += 1
        row_i += 1
    print(visible_trees)

def get_visibility(matrix, row_i, col_j):
    # row_i = 3
    # col_j = 2
    tree = matrix[row_i][col_j]
    north = 0
    east = 0
    south = 0
    west = 0

    # north
    for i in range(row_i -1, -1, - 1):
        north_tree = matrix[i][col_j]
        # print(north_tree)
        north += 1
        if north_tree >= tree:
            break

    # east
    for j in range(col_j + 1, len(matrix[0])):
        east_tree = matrix[row_i][j]
        # print(east_tree)
        east += 1
        if east_tree >= tree:
            break

    # south
    for i in range(row_i + 1, len(matrix)):
        south_tree = matrix[i][col_j]
        south += 1
        if south_tree >= tree:
            break

    # west
    for j in range(col_j -1, -1, -1):
        west_tree = matrix[row_i][j]
        # print(west_tree, row_i, j)
        west += 1
        if west_tree >= tree:
            break

    # print(tree, north, east, south, west)
    return north * east * south * west

def day_two(matrix):
    row_max = len(matrix) -1
    col_max = len(matrix[0]) -1
    row_i = 0
    best_visibility = 0

    for row in matrix:
        if row_i == 0 or row_i == row_max:
            row_i += 1
            continue
        col_j = 0
        for col in row:
            if col_j == 0 or col_j == col_max:
                col_j += 1
                continue
            score = get_visibility(matrix, row_i, col_j)
            # print(score)
            # return
            if score > best_visibility:
                best_visibility = score
            col_j += 1
        row_i += 1
    print(best_visibility)

def main():
    lines = read_all_lines("in.txt")
    matrix = build_matrix(lines)
    # day_one(matrix)
    day_two(matrix)

if __name__ == "__main__":
    main()