from collections import defaultdict

PRECALC = {str(k): k ** 2 for k in range(10)}

def next_in_chain(n):
    '''
        Return the next element in square digit chain
    '''
    return sum(PRECALC[k] for k in str(n))

def problem():
    '''
        Return the count of numbers < 10 ** 7 that will arrive at 89
        in the square digit chain.

        Brute forced, but only calculated the chains of 1,..,567 since

            9^2 * 9 = 567.

    '''
    ends_in_89 = [0] * (568)
    count = 0
    for n in range(1, 568):
        m = next_in_chain(n)
        while m not in (1, 89):
            m = next_in_chain(m)
        if m == 89:
            ends_in_89[n] = 1
            count += 1
    for n in range(568, 10 ** 7):
        count += ends_in_89[next_in_chain(n)]
    return count

if __name__ == "__main__":
    print(problem())
        
