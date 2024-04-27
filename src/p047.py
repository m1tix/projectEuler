def factor_all(b):
    '''
        Returns the factorisation of all positive numbers <= b larger than 1.
        Not putting this in utils, very ugly please ignore
    '''
    divisors = [[] for _ in range(b + 1)]
    for i in range(2, b + 1):
        if not divisors[i]:
            divisors[i].append(i)
            for j in range(2 * i, b + 1, i):
                divisors[j].append(i)
    return divisors

def problem(b):
    '''
        Returns the smallest number n <= b such that n, n + 1, n + 2, n + 3 and
        are all composite numbers with exactly 4 prime factors. Returns None if
        such an n does not exist.
    '''
    candidates = factor_all(b)
    for i, divs in enumerate(candidates):
        if len(divs) == 4:
            for j in range(1, 4):
                if len(candidates[i + j]) != 4:
                    break
            else:
                return i
    return None


if __name__ == "__main__":
    print(problem(10 ** 6))
