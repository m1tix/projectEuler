def problem(n):
    '''
        Returns the largest palindrome nummer smaller than n that is a product
        of two 3-digit numbers. Implementation is quite inefficient but
        whatever. Also assumes that n > smallest palindrome, or else it does
        not return a valid answer.
    '''
    palin_list = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if str(num) == str(num)[::-1]:
                palin_list.append(num)
    return max(list(filter(lambda x: x < n, palin_list)))


if __name__ == "__main__":
    print(problem(10**6))
