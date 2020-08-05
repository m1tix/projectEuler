def problem017(n):
    '''
        Returns the integer n as a word, e.g. problem017(2) returns Two.
        Oh, n is bounded by 0 and 10**12 (trillion)
        Note that this is actually the Hackerrank challenge not the Project
        Euler. If it was, then it could be optimized by quite a large margin

        This should be looked at again, absolute mess of a function
    '''
    def small_thousand(n):
        if n < 20:
            return smallNumbers[n]
        if n < 100:
            if n % 10 == 0:
                return twoDigits[n // 10 - 2]
            rem = n // 10
            return twoDigits[rem - 2] + " " + smallNumbers[n - 10*rem]
        rem = n // 100
        if n % 100 == 0:
            return smallNumbers[rem] + " hundred"
        return smallNumbers[rem] + " hundred " + small_thousand(n - 100*rem)

    smallNumbers = ("zero", "one", "two", "three", "four", "five", "six",
                    "seven", "eight", "nine", "ten", "eleven", "twelve",
                    "thirteen", "fourteen", "fifteen", "sixteen",
                    "seventeen", "eighteen", "nineteen")
    twoDigits = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                 "eighty", "ninety")
    powersTen = ("thousand", "million", "billion", "trillion")
    nString = ""
    for k in range(12, 2, -3):
        rem = n // 10**k
        if rem != 0:
            nString += small_thousand(rem) + " " + powersTen[k // 3 - 1] + " "
            n = n - rem*10**k
    if n != 0:
        nString = nString + small_thousand(n)
    return nString.title()


if __name__ == "__main__":
    sumNumbers = 0
    for i in range(1, 1001):
        stri = problem017(i)
        sumNumbers += len(stri.replace(' ', ''))
    print(sumNumbers + 99*9*3)
