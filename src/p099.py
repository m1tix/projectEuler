from pathlib import Path
from math import log

def compare_exponent(exp1, exp2):
    '''
        Returns True if a^b > c^d, False otherwise.
    '''
    return exp1[1] * log(exp1[0]) > exp2[1] * log(exp2[0])

def problem(exps):
    '''
        From a list of bases and exponents, return the maximum element.

        Very easy problem: just take logs.... (might even be able to brute-force it
        with todays computing power).
    '''
    curr_max = (0, 0, 0)
    for i, row in enumerate(exps.split('\n')):
        exp = tuple(int(k) for k in row.split(','))
        if i == 0:
            curr_max = (i, exp)
            continue
        if compare_exponent(exp, curr_max[1]):
            curr_max = (i, exp)
    return curr_max[0] + 1

def insertion(exp_list, exp_list_length, exp):
    '''
        Returns the index where exp can be inserted such that
        exp_list is still sorted. Algorithm is binary search.
    '''
    left = 0
    right = exp_list_length - 1
    while left <= right:
        i = (left + right) // 2
        if compare_exponent(exp, exp_list[i]):
            left = i + 1
        else:
            right = i - 1
    return left

def problem_hackerrank(exps, k):
    '''
        From a list of bases and exponents, return the k-th element
    '''
    res = []
    for i, row in enumerate(exps.split('\n')):
        exp = tuple(int(k) for k in row.split(','))
        insertion_index = insertion(res, i, exp)
        res.insert(i, exp)
    return res[k - 1]

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/099.txt", "r") as f:
        content = f.read()
    print(problem(content))

