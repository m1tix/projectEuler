
def problem002(n):
    '''
        Returns the sum of the even fibonacci numbers not exceeding n
    '''
    E = [0, 2]
    sumE = sum(E)
    while E[1] < n:
        newE = 4*E[1] + E[0]
        if newE >= n:
            break
        sumE += newE
        E = [E[1], newE]
    return sumE


if __name__ == "__main__":
    print(problem002(4*10**6))
