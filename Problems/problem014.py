def problem014(n):
    '''
        Returns an integer k <= n which has the largest Collatz-sequence.
        Runs through all integers to n and calculate the Collatz-sequence. To
        do this efficiently, we store both the length of the n-th
        Collatz-sequence in collatzLength[n] and the current largest integer in
        the largest list for which the Collatz-sequence is the longest.
    '''
    collatzLength = [0, 1, 2] + [0] * (n - 2)
    largest = [0, 1, 2] + [0] * (n - 2)
    for k in range(3, n + 1):
        newk = k
        currLength = 0
        while newk != 1:
            if newk < n and collatzLength[newk] != 0:
                finalLength = collatzLength[newk] + currLength
                collatzLength[k] = finalLength
                if finalLength >= collatzLength[largest[k - 1]]:
                    largest[k] = k
                else:
                    largest[k] = largest[k - 1]
                break
            currLength += 1
            if newk % 2:
                newk = 3 * newk + 1
            else:
                newk = newk >> 1
    return largest


if __name__ == "__main__":
    print(problem014(10**6)[10**6])
