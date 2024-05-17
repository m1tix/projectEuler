def problem(k):
    '''
        Returns the last k digits of the massive non-Mersenne prime

            28433 * 2 ^ 7830457 + 1

        With todays computing power this is too easy. Yet I reckon the desired approach would be
        to compute modulo 10 ** k.
    '''
    return (28433 * pow(2, 7830457, 10 ** k) + 1) % 10 ** k

if __name__ == "__main__":
    print(problem(12))
