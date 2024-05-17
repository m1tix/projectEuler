from copy import deepcopy
from pathlib import Path

DIGITS = {1,2,3,4,5,6,7,8,9}

def build_cell_data(sudoku):
    digits_rows = [DIGITS - set(sudoku[i]) for i in range(9)]
    digits_cols = [DIGITS - set([sudoku[j][i] for j in range(9)]) for i in range(9)]
    digits_square = [DIGITS - set.union(*[set(sudoku[3*(n // 3) + i][3*(n % 3):3*((n % 3) + 1)])
        for i in range(3)]) for n in range(9)]
    cell_data = dict()
    filled_cells = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                available_digits = digits_rows[i] & digits_cols[j] & digits_square[3 * (i // 3) + j // 3]
                cell_data[(i,j)] = available_digits
            else:
                filled_cells += 1
    return cell_data, filled_cells


def update_cell_data(cell, val, sudoku, cell_data):
    '''
        Update the coordinate of the given sudoku to val and update
        the cell_data inplace.
    '''
    i, j = cell
    sudoku[i][j] = val
    # remove val from all cells in the same row/column
    for n in range(9):
        if sudoku[i][n] == 0:
            cell_data[(i,n)] -= set({val})
        if sudoku[n][j] == 0:
            cell_data[(n,j)] -= set({val})
    # remove val from all cells in the same square
    for n in range(9):
        t = (3*(i // 3) + n // 3, 3 * (j // 3) + (n % 3))
        if sudoku[t[0]][t[1]] == 0:
            cell_data[t] -= set({val})
    del cell_data[cell]


def problem(sudoku):
    '''
        Returns a solved version of the given sudoku. Method may take long in case there is a lot
        of backtracking. The idea behind it is quite simple however: create a dictionary for all
        cells indicating the possible entries. Then loop over this dictionary and check if there are any
        cells with just one possible entry: if so, fill it in. If not, then our next best step would be to
        guess some entry. Since there is possibility of failure, we save the current state to a list 
        and restore this state if we encounter any unfilled cell with no possible entries.
    '''
    cell_data, filled_cells = build_cell_data(sudoku)
    backtracking = []
    while filled_cells != 81:
        temp = dict(cell_data)
        min_options = ((0, 0), 9)
        for cell, val in temp.items():
            if val == set():
                # The given cell has no possible values
                # thus we must backtrack
                last_state = backtracking.pop()
                cell_data, filled_cells = build_cell_data(last_state[2])
                sudoku = last_state[2]
                cell_data[last_state[0]] -= set({last_state[1]})
                break
            if len(val) != 1:
                if min_options[1] > len(val):
                    min_options = (cell, len(val))
                continue
            val = val.pop()
            update_cell_data(cell, val, sudoku, cell_data)
            filled_cells += 1
            break
        else:
            # There is no cell with just a single option, hence we must 'guess'
            # optimally we guess a value for a cell which has the minimal number
            # of possible values, i.e. min_options[0]
            val = cell_data[min_options[0]].pop()
            t = deepcopy(sudoku)
            backtracking.append((min_options[0], val, t))
            update_cell_data(min_options[0], val, sudoku, cell_data)
            filled_cells += 1
    return sudoku

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/096.txt", "r") as f:
        content = f.read().split('\n')
    res = 0
    for i in range(len(content) // 10):
        sudoku = [[int(k) for k in s] for s in content[10*i+1: 10*i + 10]]
        solved_sudoku = problem(sudoku)
        res += sum(10 ** (3 - i - 1) * solved_sudoku[0][i] for i in range(3))
    print(res)
