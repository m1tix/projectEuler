from pathlib import Path

VALUES = {'T': 10, 'J': 11, 'Q' : 12, 'K' : 13, 'A': 14}
VALUES.update({str(k) : k for k in range(2, 10)})

def occurences(l):
    '''
        Return a dictionary of the number of occurences of each element in the list l.
    '''
    count = dict()
    for x in l:
        try:
            count[x] += 1
        except KeyError:
            count[x] = 1
    return count

def eval_hand(hand):
    '''
        Evaluate the given (VALID) hand. Input should be a list of 5 tuples (x, y),
        where x is the value of the card and y the suite (D/H/C/S).
        Possible outputs:
            1: High card;
            2: Pair;
            3: Two pair;
            4: Three of a kind;
            5: Straight;
            6: Flush;
            7: Full house;
            8: Four of a kind;
            9: Straight Flush or ROYAL flush.
    '''
    values, suites = list(zip(*sorted(hand, key=lambda x: x[0], reverse=True)))
    # really ugly but necessary for comparison of lowest straight
    # First check for flushes and straight as they require all 5 cards
    is_flush = len(set(suites)) == 1
    is_straight = values == (14, 5, 4, 3, 2) or values == tuple(range(values[0], values[-1] - 1, -1))
    # note that has to be values[1], else the lowest straight (14, 5, 4, 3, 2) is scored higher
    # then second-to-lowest straight (6,5,4,3,2).
    if is_straight and is_flush:
        return 9, values[1]
    if is_flush:
        return 6, values
    if is_straight:
        return 5, values[1]

    # Now check for pairs and three of a kinds
    threes = []
    pairs = []
    occurence_values = occurences(values)
    for v in occurence_values:
        if occurence_values[v] == 4:
            return 8, v
        elif occurence_values[v] == 3:
            threes.append(v)
        elif occurence_values[v] == 2:
            pairs.append(v)
    if threes and pairs:
        return 7, threes[0], pairs[0]
    if threes:
        return 4, threes[0]
    if pairs:
        return len(pairs) + 1, *pairs, values
    return 1, values

def problem(hands):
    '''
        Returns the count of how many times player 1 wins. Hands should be a list of strings
        each consisting of 2 hands, one of player 1 and another of player 2.

        Note:
            - If two players play a flush, the player with the highest card wins.
    '''
    wins = 0
    for play in hands:
        hand = [(VALUES[v[0]], v[1]) for v in play.split(' ')]
        score1 = eval_hand(hand[:5])
        score2 = eval_hand(hand[5:])
        if score1 > score2:
            wins += 1
    return wins


if __name__ == "__main__":
    with open(Path(__file__).parent / 'input/054.txt', 'r') as f:
        hands = f.read()[:-1].split('\n')
    print(problem(hands))
