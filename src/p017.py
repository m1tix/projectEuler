def problem(n):
    '''
        Returns the integer n as a word, e.g. problem017(2) returns Two.
        Oh, n is bounded by 0 and 10**12 (trillion)
        Note that this is actually the Hackerrank challenge not the Project
        Euler. If it was, then it could be optimized by quite a large margin

        This should be looked at again, absolute mess of a function
    '''

    def small_thousand(n):
        if n < 20:
            return small_numbers[n]
        if n < 100:
            if n % 10 == 0:
                return two_digits[n // 10 - 2]
            rem = n // 10
            return two_digits[rem - 2] + " " + small_numbers[n - 10 * rem]
        rem = n // 100
        if n % 100 == 0:
            return small_numbers[rem] + " hundred"
        return small_numbers[rem] + " hundred " + small_thousand(n - 100 * rem)

    small_numbers = ("zero", "one", "two", "three", "four", "five", "six",
                     "seven", "eight", "nine", "ten", "eleven", "twelve",
                     "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                     "eighteen", "nineteen")
    two_digits = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                  "eighty", "ninety")
    powers_ten = ("thousand", "million", "billion", "trillion")
    n_string = ""
    for k in range(12, 2, -3):
        rem = n // 10**k
        if rem != 0:
            n_string += small_thousand(rem) + " " + powers_ten[k // 3 -
                                                               1] + " "
            n = n - rem * 10**k
    if n != 0:
        n_string = n_string + small_thousand(n)
    return n_string.title()


if __name__ == "__main__":
    sum_numbers = 0
    for i in range(1, 1001):
        stri = problem(i)
        sum_numbers += len(stri.replace(' ', ''))
    print(sum_numbers + 99 * 9 * 3)
