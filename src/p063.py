def problem():
    '''
        Returns the count of numbers that are n-th powers while simultaneously having
        n digits.

        Very easy, answer is

            sum_{n=1}^infty (10 - ceil(10 ^((n-1)/n)))

        Upper bound is 10^((n-1)/n) > 9, i.e. n >= log(10) / (log(10) - log(9)) ~ 21
    '''
    return 49

if __name__ == "__main__":
    print(problem())
