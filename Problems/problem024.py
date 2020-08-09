from math import factorial


def problem024(n, k):
    '''
        Returns the k-th lexicographic permutation of [0,1,2,...,n].
        Also, this method was first done by hand for n = 9 and k=10**6. It was
        subsequently extended to all n and k because why not.
    '''
    def helpf(k, availNumbers):
        n = len(availNumbers)
        if n == 1:
            return [availNumbers[0]]
        i = max(filter(lambda x: x * factorial(n - 1) < k, range(n + 1)))
        letter = [availNumbers.pop(i)]
        return letter + helpf(k - i * factorial(n - 1), availNumbers)

    numbers = list(range(n + 1))
    if k > factorial(n + 1):
        return 'k is too big'
    return helpf(k, numbers)


if __name__ == "__main__":
    print(problem024(9, 1))
