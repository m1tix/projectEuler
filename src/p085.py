from math import floor, sqrt


def problem(b):
    '''
        Returns the largest area of a grid who contains the closest
        to b amount of rectangles.

        Let R^{n,m}(i, k) denote the number of rectangles
        of size i times k which can fit into a grid of n by m. Assuming that
        a rectangle lies in the upper corner of the grid, we can shift it (n - i)
        times horizontally and (m - k) times vertically. Hence

            R^{n,m}(i,k) = (n + 1 - i)(m + 1 - k)

        Summing over all possible rectangles gives us the number of rectangles
        S that fits into the grid:
            
            S = sum_{i,k} R^{n,m}(i,k) = n * (n + 1) * m * (m + 1) / 4.

        Now, without loss of generality we may assume that n >= m. Thus

            m^2 (m + 1)^2 <= 4b,

        that is, m <= sqrt(sqrt(4b) + 1/4) - 1/2
    '''
    m_bound = floor(sqrt(sqrt(4*b) + 1/4) - 1/2)
    curr_min = (2 * b, 0, 0)
    for m in range(1, m_bound + 2):
        n = round(sqrt(4 * b / (m ** 2 + m) + 1/4) - 1/2)
        diff = abs((n ** 2 + n) * (m ** 2 + m) - 4*b)
        if ((diff == curr_min[0] and m * n >= curr_min[-1]) or
                diff < curr_min[0]):
            curr_min = (diff, (m, n), m * n)
    return curr_min

if __name__ == "__main__":
    print(problem(2 * 10 ** 6)[-1])
