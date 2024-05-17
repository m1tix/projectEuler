from math import ceil, sqrt


def all_divisors(b):
    '''
        Return the sum of the proper divisors of n for all n <= b
    '''
    res = [0] + [1] * b
    for p in range(2, b + 1):
        if res[p] == 1:
            for n in range(2 * p, b + 1, p):
                p_sum = 1
                k = n
                e = 0
                while k % p == 0:
                    e += 1
                    p_sum += p ** e
                    k = k // p
                res[n] *= p_sum
    # Should find a way such that this loop is unnecessary
    for n in range(4, b + 1):
        if res[n] != 1:
            res[n] -= n
    return res

def problem(b):
    '''
        Return the smallest element from the largest amicable chain that does not exceed b.
        Fairly simple algorithm, basically brute forcing but with a few optimizations.

        Shaved of 2 seconds so far by optimizing all_divisors. Then used memoiziation for 
        the numbers that are seen.

        Previous time: ~8.16seconds (3 trials)
        Current time: ~4.67seconds (3 trials)
    '''
    sum_divisors = all_divisors(b)
    curr_max = (0, [0])
    for n in range(2, b + 1):
        curr_chain = [n]
        while True:
            next = sum_divisors[curr_chain[-1]]
            if next in curr_chain:
                for v in curr_chain:
                    sum_divisors[v] = 1
                sub_chain = curr_chain[curr_chain.index(next):]
                if len(sub_chain) > curr_max[0]:
                    curr_max = (len(sub_chain), sub_chain)
                break
            if next > b or next == 1:
                for v in curr_chain:
                    sum_divisors[v] = 1
                break
            curr_chain.append(next)
    return min(curr_max[1])

if __name__ == "__main__":
    print(problem(2 * 10 ** 6))
