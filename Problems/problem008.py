from math import prod


def problem008(n, k):
    '''
        Returns the largest product of k consecutive digits in n
    '''
    if n < k:
        raise ValueError('n is too small')
    entries = [str(n)[i:i+k] for i in range(len(str(n)) - k + 1)]
    return max(map(lambda x: prod(int(i) for i in x), entries))


if __name__ == "__main__":
    with open("Inputs/problem008.txt") as f:
        numberText = f.read().splitlines()
    num = int(''.join(numberText))
    print(problem008(num, 13))
