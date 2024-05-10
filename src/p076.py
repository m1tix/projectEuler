from math import floor, sqrt


def problem(n):
    '''
        Returns the number of ways n can be written as a sum of non-negative integers.

        In other words, the number of partitions p_n of n. Note that the generator function
        of the partition function is equal to

            prod_{k >= 1}(1 + x^k + x^{2k} + ...) = prod_{k >= 1} (1 - x^k)^{-1},

        while by Euler's pentagonal theorem we have

            prod_{k >= 1} (1 - x^k) = 1 + sum_{k >= 1} (-1)^k (x^{g_k} + x^{g_{-k}})

        where g_k is the k-th pentagonal number. It thus follows that

            p_n = sum_{k != 0} (-1)^{k-1} p_{n - g_k}

        which allows for a recursive computation.
    '''
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    pentagonals = [(k * (3 * k - 1) // 2, k * (3 * k + 1) // 2) 
        for k in range(1, floor((sqrt(24 * n - 1) + 1) / 6) + 1)]
    for k in range(2, n + 1):
        curr_val = 0
        for i, ps in enumerate(pentagonals):
            for p in ps:
                if p <= k:
                    curr_val += (-1) ** i * res[k - p]
        res[k] = curr_val
    return res[n]


if __name__ == "__main__":
    print(problem(100) - 1)
