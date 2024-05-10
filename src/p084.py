import numpy as np


def construct_matrix():
    '''
        Construct the markov chain of monopoly
        I have given up on vectorizing this: idk how

        Order is as follows:
            - res is a 120 by 120 matrix representing the chance of going
                from square i to square j.
            - Every square, except the special squares (jail, chance, community)
                are represented thrice: once for every possible state of rolling doubles.

        Abandoned for now, dont like this problem....

    '''
    probs = (0, 0, 0, 1/18, 1/18, 1/9, 1/9,1/6,1/9,1/9,1/18,1/18, 0)
    double_probs = (0, 0, 1/36, 0, 1/36, 0, 1/36, 0, 1/36, 0, 1/36, 0, 1/36)
    res = np.zeros((120, 120))
    for i in range(40):
        for j in range(13):
            if i not in (2,7,10,17,22,33,36):
                # normal roll to next square
                res[i][(i + j) % 40] = probs[j]
                res[i][(i + j) % 40 + 40] = double_probs[j]
                # Have rolled a double 
                res[i + 40][(i + j) % 40] = probs[j]
                res[i + 40][(i + j) % 40 + 80] = double_probs[j]
                # Have rolled two doubles
                res[i + 80][(i + j) % 40] = probs[j]
            # community chest
            else: 
                if i in (2, 17, 33):
                    res[i][0] = 1/16
                    res[i][50] = 1/16
                    res[i][i + 40] = 14/16
            # chance
                elif i in (7, 22, 36):
                    res[i][0] = 1/16
                    res[i][10] = 1/16
                    res[i][11] = 1/16
                    res[i][24] = 1/16
                    if i == 36:
                        res[i][5] = 3/16
                    else:
                        res[i][5] = 1/16
                    if i == 7:
                        res[i][15] = 2/16
                    if i == 22:
                        res[i][25] = 2/16
                        res[i][28] = 1/16
                    else:
                        res[i][12] = 1/16
                    res[i][39] = 1/16
                    res[i][i - 3] = 1/16
                    res[i][i + 40] = 6/16
                res[i + 40][(i + j) % 40] = probs[j]
                res[i + 40][(i + j) % 40 + 40] = double_probs[j]
        # Chance to go to jail after 2 doubles
        res[i + 80][10] = sum(double_probs)
    # Once in jail, we have to wait a single turn.
    res[10][50] = 1
    test = np.sum(res, axis=1)
    for i in range(len(test)):
        if test[i] != 1:
            print(i, test[i])
    return res

def problem():
    pass

if __name__ == "__main__":
    construct_matrix()
