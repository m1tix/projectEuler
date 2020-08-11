def problem028(n):
    '''
        Returns the sum of diagonal elements in a n by n spiral.
        Denote a_k as the sum of the lower right and upper right element in the
        spiral on layer k, where we start counting from k = 0.
        It is easy to see that

            a_k = (2k+1)^2 + (2k-1)^2 + 2k = 8k^2+2k+2.

        By writing n = 2m+1 (as n has to be odd) we find the answer is equal to

            2sum_{k=1}^m a_k + 1 = 2/3m(8m^2+15m+13) + 1,

        one can check this with induction :).
    '''
    assert (n - 1) % 2 == 0
    if n == 1:
        return 1
    m = (n - 1) // 2
    return 2 * m * (8 * m**2 + 15 * m + 13) // 3 + 1


if __name__ == "__main__":
    print(problem028(1001))
