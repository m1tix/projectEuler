from collections import defaultdict
from math import factorial

PRECALC = {str(k) : factorial(k) for k in range(10)}

def next_in_chain(n):
    return sum(PRECALC[k] for k in str(n))

def problem(b):
    '''
        Returns the count of all numbers <= b that have exactly a digit factorial
        chain of length 60.

        Very straightforward code: loop over all numbers and store the length of all found
        chains in a dictionary for ease of access.
    '''
    length_dict = defaultdict(int)
    length_dict[2] = 1
    length_dict[169] = 3
    count = 0
    for n in range(1, b + 1):
        curr = [n]
        m = n
        offset = 0
        while next_in_chain(m) not in curr:
            m = next_in_chain(m)
            if length_dict[m] != 0:
                offset = length_dict[m]
                break
            curr.append(m)
        for i, k in enumerate(curr):
            if k == next_in_chain(m):
                break
            if length_dict[k] == 0:
                length_dict[k] = len(curr) - i + offset
                if length_dict[k] == 60:
                    count += 1
    return count


if __name__ == "__main__":
    print(problem(10 ** 6))
