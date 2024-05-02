def problem(n):
    '''
        Returns the sum of the digits of the n-th convergent of
        e. To solve HackerRank version, increase max digits with
        sys.set_int_max_str_digits()


        Note that e = [2, 1, 2, 1, 1, 2, 1, 1, 4, ...], which can be deducted
        from the continued fraction representation of tanh [1].

        [1] https://topologicalmusings.wordpress.com/2008/08/04/continued-fraction-for-e/
    '''
    # we only need the numerator of the convergents
    p_prev, p_new = 1, 2
    for i in range(1, n):
        ai = (1, 1, 2 * ((i // 3) + 1))[i % 3]
        p_prev, p_new = p_new, ai * p_new + p_prev
    return sum(int(d) for d in str(p_new))

if __name__ == "__main__":
    print(problem(10 ** 2))
