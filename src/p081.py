from pathlib import Path


def problem(mat):
    '''
        Returns the minimal path sum from the top left corner of the given
        matrix to the bottom right corner, by only moving right or down.

        Basically a simple dynamic programming exercise: by working from the
        bottom right corner the minimal path sum from the (i, j)-th position
        in the matrix is the value at (i, j) plus the minimum value of the
        two adjecent nodes. We can thus go over the matrix and iteratively update, in-place,
        the values until we reach (0,0).

        Can also use any path finding algorithm, but seems rather overkill.
    '''
    rows = len(mat)
    columns = len(mat[0])
    for i in range(rows - 1, -1, -1):
        for j in range(columns - 1, -1, -1):
            if i == rows - 1 and j == columns - 1:
                continue
            elif i == rows - 1:
                mat[i][j] += mat[i][j + 1]
            elif j == columns - 1:
                mat[i][j] += mat[i+1][j]
            else:
                mat[i][j] += min(mat[i][j+1], mat[i+1][j])
    return mat[0][0]


if __name__ == "__main__":
    with open(Path(__file__).parent / "input/081.txt", "r") as f:
        content = f.read()[:-1]
    mat = [list(map(int, row.split(','))) for row in content.split('\n')]
    print(problem(mat))
