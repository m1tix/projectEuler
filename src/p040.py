def champernowne(k):
    '''
        Returns the k-th digit in the Champernowne constant.
    '''
    m = 1
    t = 0
    # Determines the number of digits m of the number that the k-th
    # digit belongs to. Ex: if k = 12, then k belongs to the number 11,
    # which has two digits.
    # t is the beginning of the m-th digits in the string.
    while k > t + 9 * 10 ** (m - 1) * m:
        t += 9 * 10 ** (m - 1) * m
        m += 1
    offset = (k - t - 1) % m
    return int(str((k - t - 1) // m + 10 ** (m - 1))[offset])


def problem(indices):
    '''
        Computes the i-th digit in the Champernowne constant for each
        i in an enumerable indices and returns their product.
    '''
    prod = 1
    for i in indices:
        prod *= champernowne(i)
    return prod

if __name__ == "__main__":
    print(problem([1, 10, 100, 1000, 10000, 100000, 1000000]))
