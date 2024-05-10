def problem(target):
    '''
        Returns the number of possible ways we can construct m pence from
        the 8 standard coins: 1, 2, 5, 10, 20, 50, 100 and 200.
    '''
    res = [1] + [0] * target
    vals = (1, 2, 5, 10, 20, 50, 100, 200)
    for val in vals:
        # res[n] is number of ways we can make n pence from our selected coin
        # we thus iteratively update this value while looping over the coins
        for i in range(target - val + 1):
            res[val + i] += res[i]
        print(res)
    return res[target]


if __name__ == "__main__":
    print(problem(200))
