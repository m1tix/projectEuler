from math import comb


def problem015(n, m):
    '''
        Returns the number of paths in a (n x m)-grid starting from the top
        left corner and ending in the lower right corner while only moving
        right or down.
        First note that any path contains n + m steps along the edges of the
        squares. Secondly note that any path must exactly have m steps down or
        else it would not reach the lower right corner. Since the order of
        these steps does not matter, the final answer is (n + m choose m)
    '''
    return comb(n + m, m)


if __name__ == "__main__":
    print(problem015(20, 20))
