def problem(triangle):
    '''
        Returns the largest sum from top to bottom in a triangle
    '''
    if len(triangle) == 1:
        return triangle[0][0]
    last_row = triangle[-1]
    upper_row = triangle[-2]
    for i, _ in enumerate(upper_row):
        largest = max(last_row[i:i + 2])
        upper_row[i] += largest
    triangle = triangle[:-2] + [upper_row]
    return problem(triangle)


if __name__ == "__main__":
    trgl = []
    with open('input/018.txt', 'r') as f:
        for line in f:
            trgl.append([int(entry) for entry in line.split(' ')])
    print(problem(trgl))
