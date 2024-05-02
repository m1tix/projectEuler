import re

from utils import utils

def digit_count(n):
    '''
        Return the count of each digit as a dictionary
    '''
    digits = {str(k) : 0 for k in range(10)}
    for d in n:
        digits[d] += 1
    return digits

def problem():
    '''
        Return the smallest prime, which by replacing part of the number with the same
    digit, is part of an eight prime value family.

    Some observation:
        - Have to replace more than 1 digit;
        - Cannot replace the last digit.
        - Cannot replace an even amount of digits (divisibility by three [sum of digits!]).

    Not entirely correct: can be 5 digits repeating pattern.
    '''
    is_prime = utils.sieve_eratosthenes_raw(10 ** 6)
    for i in range(56000, 10 ** 6 + 1):
        if not is_prime[i]:
            continue
        digits = digit_count(str(i)[:-1])
        if max(digits.values()) == 3:
            rep_digit = max(digits, key=digits.get)
            final_digit = int(str(i)[-1])
            prime_count = 0
            for d in range(10):
                new_i = int(re.sub(rep_digit, str(d), str(i)[:-1], 0))
                poss_prime = 10 * new_i + final_digit
                # > 10 ** 4 condition necessary, else trailing zeros count!
                if is_prime[poss_prime] and poss_prime > 10 ** 4:
                    prime_count += 1
            if prime_count >= 8:
                return i

if __name__ == "__main__":
    print(problem())
