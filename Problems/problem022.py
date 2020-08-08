def problem022(nameList):
    '''
        Let nameList be an alphebetically sorted list of names in uppercases.
        This function returns the total of all name scores of names in
        nameList. The name score of a name is the position of that name in the
        list multiplied by the alphebetical value of that name.
    '''
    totalScore = 0
    scoreDict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
                 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                 'Z': 26}

    def name_score(name):
        return sum(map(lambda x: scoreDict[x], name))
    for pos, name in enumerate(nameList):
        totalScore += (pos + 1)*name_score(name)
    return totalScore


if __name__ == "__main__":
    with open("Inputs/problem022.txt", "r") as f:
        rawText = f.read().replace("\"", "").split(",")
    # python do be easy
    rawText.sort()
    print(problem022(rawText))
