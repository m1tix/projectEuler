def problem(n, b):
    '''
        Returns the sum of all numbers less than N which are palindromic in
        base 10 and base b with 2 <= b <= 9.
    '''

    def to_base(n, b):
        if n == 0:
            return ""
        return to_base(n // b, b) + str(n % b)

    palindromic_sum = 0
    for k in range(1, n):
        if (str(k)[::-1] == str(k)
                and str(to_base(k, b))[::-1] == str(to_base(k, b))):
            palindromic_sum += k
    return palindromic_sum


if __name__ == "__main__":
    print(problem(10**6, 2))
