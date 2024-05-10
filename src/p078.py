def pentagonals():
    '''
        Generate the pentagonal numbers. Rather inefficient as it calculates
        a square each loop, but whatever.
    '''
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        yield n * (3 * n + 1) // 2
        n += 1


def problem():
    '''
        Return the smallest integer n such that p(n) is divisible by one million.
        In other words, the smallest integer n such that the number of partitions
        is divisible by one million. Hence exact same thing as p76.
    '''
    res = [1, 1]
    n = 2
    while res[n - 1] != 0:
        curr_val = 0
        for i, p in enumerate(pentagonals()):
            if p > n:
                break
            curr_val += (-1) ** (i // 2) * res[n - p]
        res.append(curr_val % 10 ** 6)
        n += 1
    return n - 1

if __name__ == "__main__":
    print(problem())
