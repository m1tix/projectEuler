from collections import defaultdict

def problem(k, b):
    '''
        Return the smallest cube for which exactly k permutations of its digits are cubes.
        Searches all cubes n^3 with n <= b.
    '''

    permutations_cubed = defaultdict(list)
    for n in range(1, b + 1):
        string_cubed = ''.join(sorted(str(n ** 3)))
        permutations_cubed[string_cubed].append(n)
        if len(permutations_cubed[string_cubed]) == k:
            return permutations_cubed[string_cubed][0] ** 3
    return 'No valid answer found, increase bound'

if __name__ == "__main__":
    print(problem(5, 10 ** 5))
