def problem():
    '''
        Return the smallest positive integer x such that kx has
        same digits as x for k = 2,...,6.
        It is well-known that this is simply the the repeating part of
        1/7
    '''
    return str(1 / 7)[2:8]

if __name__ == "__main__":
    print(problem())
