from itertools import combinations, permutations
from operator import mul, truediv, add, sub

OPS = [mul, add, sub, truediv]

def generate_all_expressions(nums):
    '''
        Generate all expressions which can be made from the list nums and the default operations
        multiplication, addition, division and subtraction.
    '''
    res = []
    pairs = permutations(nums, 2)
    # base case
    for p in pairs:
        for op in OPS:
            try:
                res.append([op(p[0], p[1]), {p[0], p[1]}])
            except ZeroDivisionError:
                continue
    # Induction
    for _ in range(2):
        curr = []
        for r in res:
            digits_left = nums - r[1]
            for c in digits_left:
                for op in OPS:
                    try:
                        curr.append([op(r[0], c), set.union(r[1], {c})])
                    except ZeroDivisionError:
                        pass
                    try:
                        curr.append([op(c, r[0]), set.union(r[1], {c})])
                    except ZeroDivisionError:
                        pass
        res = curr
    return set(r[0] for r in res)


def problem():
    '''
        Returns the the number abcd, where a < b < c < d are digits in [1...9], such that
        all numbers from 1 to n, with n maximal, can be expressed from some combination
        of a, b, c and d together with the elementary operations *, +, - and /

        Simple brute force: first generate all expressions of the form
        a.b for all pairs (a, b) and all operations .
        Then compute a.b$c for all c not equal to (a, b) and for all operations $.
        Do this repeatdly for all options and then count the number of consecutive
        natural numbers.

        Not the 'nicest' code, but functions ok. Might have been better to use reverse polish notation
        and work with templates.
    '''
    all_tuples = combinations((0,1,2,3,4,5,6,7,8,9), 4)
    curr_max = (0, 0)
    for t in all_tuples:
        res = generate_all_expressions(set(t))
        n = 1
        while n in res:
            n += 1
        if n - 1 > curr_max[0]:
            curr_max = (n - 1, t)
    return curr_max[1]
if __name__ == "__main__":
    print(problem())
