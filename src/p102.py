from pathlib import Path


def problem(triangles):
    '''
        Given a list of triangles, return the number of triangles which contain (0, 0) in
        their interior.

        I first thought of ray-tracing, but triangles are actually convex hence it is actually
        sufficient to check if for all triangle sides, the point lies to the left (or right) of the side.
    '''
    count = 0
    line_indices = [(0,1), (1, 2), (2, 0)]
    for triangle in triangles:
        prev_sign = None
        for s, t in line_indices:
            cross_prod = -(triangle[2*t] - triangle[2*s]) * triangle[2 * s + 1] + \
                (triangle[2*t+1] - triangle[2*s+1])*triangle[2*s]
            curr_sign = cross_prod > 0
            if prev_sign is None:
                prev_sign = curr_sign
            if prev_sign != curr_sign:
                break
        else:
            count += 1
    return count

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/102.txt", "r") as f:
        content = list(map(lambda x: [int(k) for k in x.split(',')], f.read()[:-1].split('\n')))
    print(problem(content))
