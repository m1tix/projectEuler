
def problem011(grid):
    '''
        Returns the greatest product of four adjacent numbers in some direction
        of the 20x20 grid with 2 digit numbers as elements
    '''
    # Pad the grid such that boundary cases are non-existence
    grid.extend([[0]*20]*3)
    for i, row in enumerate(grid):
        grid[i] = [0]*3 + row + [0]*3
    currMax = 0
    for i in range(20):
        for j in range(3, 23):
            # this is awful but atleast readable?
            rightProd = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            rightDiagProd = grid[i][j]*grid[i+1][j+1] * \
                grid[i+2][j+2]*grid[i+3][j+3]
            leftDiagProd = grid[i][j]*grid[i+1][j-1] * \
                grid[i+2][j-2]*grid[i+3][j-3]
            downProd = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            maxProd = max(rightProd, rightDiagProd, leftDiagProd, downProd)
            if currMax < maxProd:
                currMax = maxProd
    return currMax


if __name__ == "__main__":
    with open("Inputs/problem011.txt") as f:
        gridText = f.read().splitlines()
    grid = []
    for r in gridText:
        grid.append([int(digit) for digit in r.split(' ')])
    print(problem011(grid))
