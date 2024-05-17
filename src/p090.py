from itertools import combinations

def is_in_configuration(cube1, cube2, t):
    '''
        Returns True if the number in the t = (t0, t1) can be represented by
        the two cubes cube1 and cube2
    '''
    if t[1] in (6, 9):
        return ((t[0] in cube1 and 6 in cube2) or (t[0] in cube1 and 9 in cube2) or
                (6 in cube1 and t[0] in cube2) or (9 in cube1 and t[0] in cube2))
    return (t[0] in cube1 and t[1] in cube2) or (t[1] in cube1 and t[0] in cube2)

def problem():
    '''
        Returns the number of distinct arrangement one could have of two cubes
        such that every square number from 1 to 9 can be represented by the two cubes.

        I first thought this can be done by hand but quickly gave up. The solution below is
        uninspired: simply brute forcing since the number of cube arrangements is 210, quite low.
    '''
    digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    cube_configurations = list(combinations(digits, 6))
    # order so I dont have to double check for t[0] = 6, 9
    all_squares = [(0, 1), (0, 4), (0, 9),
                   (1, 6), (2, 5), (3, 6),
                   (4, 9), (4, 6), (8, 1)]
    count = 0
    for i, cube1 in enumerate(cube_configurations):
        for cube2 in cube_configurations[:i]:
            for t in all_squares:
                if not is_in_configuration(cube1, cube2, t):
                    break
            else:
                count += 1
    return count


if __name__ == "__main__":
    print(problem())
