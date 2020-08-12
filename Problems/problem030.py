from itertools import combinations_with_replacement as cwr


def problem030(n):
    '''
        Returns the sum of all the numbers which can be written as the sum of
        n-th powers of their digits, where n is greater than 3. The function
        first determines all the possible configurations of digits with
        combinations_with_replacement in itertools. It subsequently calculates
        the sum of those digits to the power n and determines whether this is
        equal to the corresponding configuration.

        With this method, this function can calculate sum of all numbers that
        can be written as the 10-th powers of their digit in less than a second
    '''
    def convert(num):
        '''
            Convert an integer to an ordered tuple of its digits padded
            by zeros. While this conversion can be done with the str() function
            ,this method is faster when n gets larger.
        '''
        digitList = []
        while num != 0:
            digitList.append(num % 10)
            num = num // 10
        return tuple([0] * (n - len(digitList) + 1) + sorted(digitList))

    total = 0
    possibleDigits = cwr(range(10), n + 1)
    for perm in possibleDigits:
        sumDigits = sum(d**n for d in perm)
        digitTuple = convert(sumDigits)
        if sumDigits > 1 and digitTuple == perm:
            total += sumDigits
    return total


if __name__ == "__main__":
    print(problem030(5))
