from utils import utils

def problem(x, y, d):
    '''
        Return the closest fraction a/b to x/y with y <= d.

        Note that this is equivalent to finding a left neighbour of x/y in the d-th Farey
        sequence. It is easy to see, by induction e.g., that a/b is a left neighbour
        of x/y in some Farey sequence iff xb - ya = 1. Thus

            b = x^{-1}(1 + ya).

        This can easily be solved: Compute x^{-1} mod y with Euclidean algorithm
        and add an appropriate offset to d to retrieve b. In turn, a can be found.
    '''
    offset, _, _ = utils.extended_euclidian(x, y)
    offset = (d - offset) % y
    if offset < 0:
        offset += y
    b = d - offset
    return (x * b - 1) // y, b
    

if __name__ == "__main__":
    print(problem(3, 7, 10 ** 6))
