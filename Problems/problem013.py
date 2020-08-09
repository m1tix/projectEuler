def problem013(nList):
    '''
        Returns the first ten digits of the sum of 50 digits numbers in nList.
        BRUTEFORCE BABY PYTHON FAST
    '''
    sm = 0
    for n in nList:
        sm += int(str(n)[:12])
    return int(str(sm)[:10])


if __name__ == "__main__":
    # kinda bad that we convert from str to int to str to int, but the input of
    # hackerrank is an integer so whatever.
    with open("Inputs/problem013.txt") as f:
        numList = [int(k) for k in f.read().splitlines()]
    print(problem013(numList))
