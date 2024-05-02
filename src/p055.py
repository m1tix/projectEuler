def is_palindrome(s):
    '''
        Returns True if the given string s is a palindrome.
    '''
    return s[:len(s) // 2] == s[:(-len(s) - 1) // 2: -1]

def problem(b):
    '''
        Returns the count of natural numbers n <= b that are believed to be Lychrel numbers.
        For the purpose of this little exercise, we assume that a number is believed to be Lychrel if
        it does not form a palindrome number before 50 iterations.
    '''
    is_possibly_lynchrel = 0
    for n in range(1, b + 1):
        m = n
        for k in range(50):
            m = m + int(str(m)[::-1])
            if is_palindrome(str(m)):
                break
        else:
            is_possibly_lynchrel += 1
    return is_possibly_lynchrel


if __name__ == "__main__":
    print(problem(10 ** 4))
