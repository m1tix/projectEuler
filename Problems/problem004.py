
def problem004(n):
    '''
        Returns the largest palindrome nummer smaller than n that is a product
        of two 3-digit numbers. Implementation is quite inefficient but
        whatever. Also assumes that n > smallest palindrome, or else it does
        not return a valid answer.
    '''
    palinList = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i*j
            if str(num) == str(num)[::-1]:
                palinList.append(num)
    return max(list(filter(lambda x: x < n, palinList)))


if __name__ == "__main__":
    print(problem004(10**6))
