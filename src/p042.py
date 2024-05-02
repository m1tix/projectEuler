from pathlib import Path
from math import sqrt, floor

def problem(word_list):
    '''
        Computes the number of words in word_list that are triangular numbers
    '''
    score_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }
    score_list = list(map(lambda s: sum(score_dict[t] for t in s), word_list))
    # bound of 500 should be enough idk
    bound = 500
    is_triangle = [0] * (bound + 1)
    for n in range(1, floor(1 / 2 * (sqrt(8 * bound + 1) - 1))):
        is_triangle[n * (n + 1) // 2] = 1
    return sum(is_triangle[score] for score in score_list)

def problem_hackerrank(n):
    '''
        If n is a triangular number, return its index. Otherwise return -1.
        Note that n is a triangular iff 8n + 1 is a perfect square.
    '''
    int_sqrt = int(sqrt(8*n + 1))
    if int_sqrt ** 2 == 8*n + 1:
        return (int_sqrt - 1) // 2
    return -1

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/042.txt") as f:
        # bad hack: should strip newlines but whatever
        words = f.read()[:-1].split(',')
    print(problem(words))
