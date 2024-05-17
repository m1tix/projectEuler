from collections import defaultdict
from itertools import combinations
from math import ceil, floor, sqrt
from pathlib import Path


def permutations(w1, w2):
    '''
        Determine all permutations S such that
            w2[i] = w1[S[i]]
        for all i. Works if and only if w1 is an anagram of w2. Can force
        a check with check variable.
    '''
    perms = [[]]
    for s in w2:
        temp = []
        for p in perms:
            for j, t in enumerate(w1):
                if s == t and j not in p:
                    temp.append(p + [j])
        perms = temp
    return perms

def unique_count(s):
    # This doesnt actually work 
    # IDEA: create a mask ***** with letters a,...,z being the ones 
    # that are double. E.g., 123123 abcabc DOESNT WORK A
    '''
        Return a list of sorted integers representing the number of times a given
        digit/letter occurs in the string s.
        EX:
            s = 'Theseus'
            unique_count(s) == [1,1,1,2,2]
    '''
    count = defaultdict(int)
    for t in s:
        count[t] += 1
    return sum(n * 10 ** i for i, n in enumerate(sorted(count.values())))


def problem(word_list):
    '''
        Two words are an anagramic square pair if both they as their numeric values are anagrams of
        each other and such that their numeric values are squares. This function finds all such pairs
        and returns the largest numeric value associated to such a pair.
    '''
    anagrams = defaultdict(list)
    for w1 in word_list:
        anagrams[''.join(sorted(w1))].append(w1)
    anagrams = sorted(filter(lambda x: len(x[1]) >= 2, anagrams.items()), key=lambda x: len(x[0]), reverse=True)
    max_digits = len(anagrams[0][0])
    squares = defaultdict(int)
    min_digits = 0
    curr_max = -1
    for k in range(1, floor(10 ** (max_digits / 2)) + 1):
        squares[k] = unique_count(str(k ** 2))
    for letters, anagram_tuple in anagrams:
        if len(letters) < min_digits:
            break
        mask = unique_count(letters)
        lower_bound = ceil(10 ** ((len(letters) - 1) / 2))
        upper_bound = floor(10 ** (len(letters) / 2))
        w1, w2 =  anagram_tuple[:2]
        perms = permutations(w1, w2)
        for k in range(lower_bound, upper_bound):
            if squares[k] == mask:
                for p in perms:
                    poss_square = int(''.join(str(k ** 2)[i] for i in p))
                    l = sqrt(poss_square)
                    if int(l) == l and len(str(poss_square)) == len(letters):
                        # min_digits = len(letters)
                        max_square = max(int(l), k)
                        print(w1, k, w2, l)
                        if curr_max < max_square:
                            curr_max = max_square
    return curr_max

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/098.txt", "r") as f:
        content = map(lambda x: x[1:-1], f.read().split(','))
    print(problem(content))
