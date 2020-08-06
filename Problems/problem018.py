def problem018(triangle):
    '''
        Returns the largest sum from top to bottom in a triangle
    '''
    if len(triangle) == 1:
        return triangle[0][0]
    lastRow = triangle[-1]
    upperRow = triangle[-2]
    # Apparently using range(len(..)) is bad form?
    for i, _ in enumerate(upperRow):
        largest = max(lastRow[i:i+2])
        upperRow[i] += largest
    triangle = triangle[:-2] + [upperRow]
    return problem018(triangle)


if __name__ == "__main__":
    trgl = []
    with open('Inputs/problem018.txt', 'r') as f:
        for line in f:
            trgl.append([int(entry) for entry in line.split(' ')])
    print(problem018(trgl))
