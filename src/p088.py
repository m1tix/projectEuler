from collections import defaultdict
from math import floor, sqrt

def problem(b):
    '''
        Return the sum of all unique 2 <= k <= b minimal product-sum numbers.

        One of the worst code I have written: first note that any
        smallest k product-sum number n must satisfy k <= n <= 2k.
        Now, we first determine all factorisations of all numbers n <= 2 * b
        and then check for each of these factorisations if it satisfies the 
        product-sum condition. To check if the factorisation of n satisfies the product-sum condition
        we just have to compute its sum, say D, and its length, say s, and set

            k = n + s - D

        This k is valid if and only if 2 <= k <= d.
    '''
    factorisations = defaultdict(list)
    for n in range(2, 2*b + 1):
        curr = []
        for d in range(2, floor(sqrt(n)) + 1):
            if n % d != 0:
                continue
            for prev in factorisations[n // d]:
                temp = sorted(prev.copy() + [d])
                if temp not in curr:
                    curr.append(temp)
        curr.append([n])
        factorisations[n] = curr
    res = [0] * (b + 1)
    zero_count = b - 1
    n = 3
    while zero_count != 0:
        n += 1
        for factorisation in factorisations[n]:
            div_sum = sum(factorisation)
            k = n + len(factorisation) - div_sum
            if 2 <= k <= b and not res[k]:
                res[k] = n
                zero_count -= 1
    return res

if __name__ == "__main__":
    res = problem(12000)
    print(sum(set(res)))
