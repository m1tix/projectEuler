from math import gcd, log, ceil, prod, sqrt
import utils


def problem1(n):
    # returns sum of multiples 3 or 5 below n
    def sfn(n):
        return int(n*(n+1))
    return (sfn((n-1)//3)*3 + sfn((n-1)//5)*5 - sfn((n-1)//15)*15) >> 1


def problem2(n):
    # returns sum of even fibonacci numbers below n >= 3
    E = [0, 2]
    sumE = sum(E)
    while E[1] < n:
        newE = 4*E[1] + E[0]
        if newE >= n:
            break
        sumE += newE
        E = [E[1], newE]
    return sumE


def problem3(n):
    # returns the largest prime factor of n >= 2
    # overkill lmao
    def pollard(n):
        a = 2
        A = a
        for i in range(2, n):
            A = pow(A, i, n)
            F = gcd(A - 1, n)
            if 1 < F < n:
                return F
        return n
    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n = n >> 1
    while n != 1:
        p = pollard(n)
        factors.append(p)
        n = n // p
    return max(factors)


def problem4(n):
    # returns the largest palindrome smaller than n that is a product of 3-
    # digits numbers (quite inefficient but whatever)
    # oh, assumes n > smallest palindrome, else it returns whoopsie
    palinList = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i*j
            if str(num) == str(num)[::-1]:
                palinList.append(num)
    return max(list(filter(lambda x: x < n, palinList)))


def problem5(n):
    # returns the smallest integer divisible by [1..n]
    multiple = 1
    for i in range(2, n+1):
        multiple = multiple*i/gcd(i, multiple)
    return multiple


def problem6(n):
    # returns the sum of first n squares minus square of the sum of the first n
    # integers
    sum1 = n*(n+1)*(2*n+1)//6
    sum2 = n*(n+1)//2

    return abs(sum1 - sum2**2)


def problem7(n):
    # returns the n-th prime, bound is a corollary of prime number theorem
    # assuming n >= 6 ;)
    primeList = utils.sieve_eratosthenes(ceil(n*log(n) + n*log(log(n))))
    return primeList[n-1]


def problem8(n, k):
    # returns the largest product of k consecutive integers in n
    if n < k:
        raise ValueError('n is too small')
    entries = [str(n)[i:i+k] for i in range(len(str(n)) - k + 1)]
    return max(map(lambda x: prod(int(i) for i in x), entries))


def problem9(n):
    # returns the largest product abc of all pythagorean triples (a,b,c) such
    # a + b + c = n. Can be optimised but whatever
    if n % 2:
        return -1
    triples = []
    for a in range(3, ceil(n/3) + 1):
        for c in range(ceil(n/3) + 1, ceil(n/2) + 1):
            b = n - a - c
            if a**2 + b**2 == c**2:
                triples.append((a, b, c))
    if triples:
        return max(d[0]*d[1]*d[2] for d in triples if d[0] + d[1] + d[2] == n)
    return -1


print(problem9(3000))
