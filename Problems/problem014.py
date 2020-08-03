def problem014(n):
    '''
        Returns an integer k <= n which has the largest Collatz-sequence.
        First stores all the Collatz-sequences in a dict and subsequently
        determines the largest integer for which this sequence is the longest.
    '''
    if n == 1:
        return 1
    collatzLength = {1: 1, 2: 2}
    largest = 2
    for k in range(2, n+1):
        newk = k
        currLength = 0
        while newk != 1:
            if newk in collatzLength:
                finalLength = collatzLength[newk] + currLength
                collatzLength[k] = finalLength
                if finalLength >= collatzLength[largest]:
                    largest = k
                break
            currLength += 1
            if newk % 2:
                newk = 3*newk + 1
            else:
                newk = newk >> 1
    return largest


if __name__ == "__main__":
    print(problem014(10**6))
