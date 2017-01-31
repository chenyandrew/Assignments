def main():

    # open file for reading
    gridfile = open("Grid.txt", "r")

    # read first line to obtain the dimensions of the square grid
    dim = gridfile.readline()
    dim = dim.strip()
    dim = int(dim)

    grid = []

    # obtain the rows of the grid
    for i in range(dim):
        line = gridfile.readline()
        line = line.strip()
        row = line.split()
        for j in range(dim):
            row[j] = int(row[j])
        grid.append(row)

    # read each row in blocks of four
    for row in grid:
        for i in range(dim - 3):
            product = 1
            for j in range(i, i + 4):
                product = product * row[j]

    # each column by blocks of four
    for i in range(dim):
        for j in range(dim - 3):
            for k in range(i, i + 4):
                column = grid[k][j]

    # major diagonal L -> R
    for i in range(dim - 3):
        for j in range(i, i + 4):
            LRdiag = grid[j][j]

    # go along diagonal L -> R in blocks of 4
    for i in range(dim - 3):
        for j in range(dim - 3):
            for k in range(4):
                LRdiagn = grid[i + k][j + k]

    # major diagonal R -> L
    for i in range(dim - 3):
        for j in range(i, i + 4):
            RLdiag = grid [j][dim - 1 - j]

    # go along diagonal R -> L in blocks of 4
    for i in range(0, dim - 3):
        for j in range(3, dim):
            for k in range(4):
                RLdiagn = grid[i + k][j - k]

    print(max(product, column, LRdiag, LRdiagn, RLdiag, RLdiagn))

    # close file
    gridfile.close()

main()
