def problem():
    '''
        Returns the value of the denominator of the four
        non-trivial cancelling fractions with two digits.
        Done by hand:
            - First determine we can only cancel fractions of the
            form
                xb
                --
                cx
            - Solve 
                10 * a + b    b
                ----------- = -
                10 * c + a    c
            - Calculate the product
                16 * 19 * 26 * 49    1
                ----------------- = ---
                64 * 95 * 65 * 98   100
    '''
    return 100


if __name__ == "__main__":
    print(problem())
