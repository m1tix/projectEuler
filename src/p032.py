from itertools import permutations, chain


def problem():
    '''
        Returns the sum of all numbers that are multiplicand/multiplier/product 
        identity pandigital 1-9.
    '''
    f = lambda x: sum(x[i] * 10 ** (len(x) - i - 1) for i in range(len(x)))
    digits = set(range(1, 10))
    pandigital_numbers = []
    # Multiplicand can only be < 99
    for c in chain(permutations(digits, 1), permutations(digits, 2)):
        digits_left = digits - set(c)
        # if multiplicand is 1 digit, then multiplier must be 4 digits
        # otherwise multiplicand has 2 digits and multiplier has 3
        for k in permutations(digits_left, 5 - len(c)):
            res = f(c) * f(k)
            # result cannot exceed 4 digits
            if res > 10 ** 4:
                continue
            digits_res = set((int(d) for d in str(res)))
            # if result and k together yield all the leftover digits,
            # then the result is pandigital 1-9
            if not digits_left - set(k) - digits_res:
                if res not in pandigital_numbers:
                    pandigital_numbers.append(res)

    return sum(pandigital_numbers)



if __name__ == "__main__":
    print(problem())
