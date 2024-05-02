from pathlib import Path

def problem(grid):
    '''
        Returns the greatest product of four adjacent numbers in some direction
        of the 20x20 grid with 2 digit numbers as elements
    '''
    # Pad the grid such that boundary cases are non-existence
    grid.extend([[0] * 20] * 3)
    for i, row in enumerate(grid):
        grid[i] = [0] * 3 + row + [0] * 3
    curr_max = 0
    for i in range(20):
        for j in range(3, 23):
            # this is awful but atleast readable? (Autoformatter fucks it up)
            right_prod = grid[i][j] * grid[i][j + 1] * grid[i][j +
                                                               2] * grid[i][j +
                                                                            3]
            right_diag_prod = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][
                j + 2] * grid[i + 3][j + 3]
            left_diag_prod = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][
                j - 2] * grid[i + 3][j - 3]
            down_prod = grid[i][j] * grid[i + 1][j] * grid[i +
                                                           2][j] * grid[i +
                                                                        3][j]
            maxProd = max(right_prod, right_diag_prod, left_diag_prod,
                          down_prod)
            if curr_max < maxProd:
                curr_max = maxProd
    return curr_max


if __name__ == "__main__":
    with open(Path(__file__).parent / "input/011.txt") as f:
        gridText = f.read().splitlines()
    gridInput = []
    for r in gridText:
        gridInput.append([int(digit) for digit in r.split(' ')])
    print(problem(gridInput))
