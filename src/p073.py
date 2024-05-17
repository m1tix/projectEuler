from math import floor

def index_in_farey_sequence(x, d):
    '''
        Determine the number of reduced proper fractions p / q <= x such that
        q <= d.
    '''
    res = [floor(x * n) for n in range(0, d + 1)]
    print(res)
    for q in range(1, d + 1):
        for mul in range(2*q, d + 1, q):
            res[mul] -= res[q]
    return sum(res)

def problem(x, y, d):
    '''
        Return the number of fractions between x > y in the d-th
        farey sequence.

        We determine the index of both x and y in the Farey sequence and then subtract
        them to yield the number of fractions between them. The idea is very simple and due
        to Patrascu: there is a one-to-one correspondence of fractions in [0, x)
        with denominator q and the reduced fractions with denominator n for all n | q. 
        If S_n denotes the number of reduced fractions with denominator n then

            floor(x q) = sum_{n | q} S_n

        Moreover, the index of x in the d-th Farey sequence is

            sum_{q=1}^d S_q = sum_{q=1}^d (floor(x q) - sum_{n | q, n < q} S_n)

        permitting a dynamic programming approach.
    '''
    return index_in_farey_sequence(x, d) - index_in_farey_sequence(y, d) - 1


if __name__ == "__main__":
    print(problem(1/3, 1/4, 120))
