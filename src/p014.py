def problem(n):
    '''
        Returns an integer k <= n which has the largest Collatz-sequence.
        Runs through all integers to n and calculate the Collatz-sequence. To
        do this efficiently, we store both the length of the n-th
        Collatz-sequence in collatzLength[n] and the current largest integer in
        the largest list for which the Collatz-sequence is the longest.
    '''
    collatz_length = [0, 1, 2] + [0] * (n - 2)
    largest = [0, 1, 2] + [0] * (n - 2)
    for k in range(3, n + 1):
        new_k = k
        curr_length = 0
        while new_k != 1:
            if new_k < n and collatz_length[new_k] != 0:
                final_length = collatz_length[new_k] + curr_length
                collatz_length[k] = final_length
                if final_length >= collatz_length[largest[k - 1]]:
                    largest[k] = k
                else:
                    largest[k] = largest[k - 1]
                break
            curr_length += 1
            if new_k % 2:
                new_k = 3 * new_k + 1
            else:
                new_k = new_k >> 1
    return largest


if __name__ == "__main__":
    print(problem(10**6)[10**6])
