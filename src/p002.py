def problem(n):
    '''
        Returns the sum of the even fibonacci numbers not exceeding n
    '''
    E = [0, 2]
    sum_e = sum(E)
    while E[1] < n:
        new_e = 4 * E[1] + E[0]
        if new_e >= n:
            break
        sum_e += new_e
        E = [E[1], new_e]
    return sum_e


if __name__ == "__main__":
    print(problem(4 * 10**6))
