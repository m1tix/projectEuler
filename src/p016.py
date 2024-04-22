def problem(n):
    '''
        Returns the sum of the digits of 2**n. The implementation is lazy
        since the bruteforce route seems to work relatively well
    '''
    return sum(int(digit) for digit in str(2**n))


if __name__ == "__main__":
    print(problem(10**3))
