def problem(b):
    '''
        Return the number n^m, with n, m < b, whose digit sum is maximal.
        Bruteforce, boring problem.
    '''
    curr_max = (0, 0)
    for n in range(1, b):
        for m in range(1, b):
            digit_sum = sum(int(k) for k in str(n ** m))
            if digit_sum > curr_max[1]:
                curr_max = (n ** m, digit_sum)
    return curr_max[1]

if __name__ == "__main__":
    print(problem(100))
