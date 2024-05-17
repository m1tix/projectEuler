from random import randint, shuffle

MAX_MOVES = 3000000

def problem(n):
    '''
        Monopoly simulator.

        First tried to construct a probability matrix, as the whole process is reminiscent
        of a markov chain. However, this turned out to be quite messy so I opted for the second best
        approach: a simple simulation. The answer is actually wrong? Program gives
        10, 15, 19, but the answer is actually 10, 15, 24 after trial and error lol.
        So uh, dont copy this as its wrong. I really dislike this problem, so I wont fix this issue.
    '''
    chance = [0, 10, 11, 24, 39, 5, "R", "R", "U", -3] + [None] * 6
    community_chest = [0, 10] + [None] * 14
    shuffle(chance)
    shuffle(community_chest)
    in_jail = False
    double_rolls = 0
    current_position = 0
    visited = {k : 0 for k in range(40)}
    for i in range(MAX_MOVES):
        visited[current_position] += 1
        if in_jail:
            in_jail = False
            continue
        die1 = randint(1, n)
        die2 = randint(1, n)
        double_rolls += (die1 == die2)
        if double_rolls == 3:
            double_rolls = 0
            in_jail = True
            current_position = 10
            continue
        current_position = (current_position + die1 + die2) % 40
        # community chest
        if current_position in (2, 17, 33):
            val = community_chest.pop()
            community_chest.insert(0, val)
            if val == 10:
                in_jail = True
                current_position = 10
            elif val == 0:
                current_position = 0
        # chance
        elif current_position in (7, 22, 36):
            val = chance.pop()
            chance.insert(0, val)
            if val == "R":
                current_position = (int(round(current_position, -1)) + 5) % 40
            elif val == "U":
                current_position = (12,28)[current_position == 22]
            elif val == -3:
                current_position = (current_position - 3) % 40
            elif val == 10:
                in_jail = True
                current_position = 10
            elif val:
                current_position = val
        # jail
        elif current_position == 30:
            current_position = 10
            in_jail = True
    return sorted(visited.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    print(problem(4))
