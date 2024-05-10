import heapq
from collections import defaultdict
from pathlib import Path


def problem(mat):
    '''
        Returns the minimal path sum starting from any value on the left column
        and finishing in any cell in the right column, and only moving up, down and/or right.

        Same setup as previous problem, but harder and our previous approach does not work.
    '''
    rows = len(mat)
    columns = len(mat[0])
    graph = defaultdict(dict)
    # first construct graph
    for i in range(rows):
        for j in range(columns):
            node = rows * i + j + 1
            if j != columns - 1:
                # right neighbour exists
                graph[node][node + 1] = mat[i][j+1]
            if i != 0:
                # upper neighbour exists
                graph[node][node - rows] = mat[i - 1][j]
            if i != rows - 1:
                # down neighbour exists
                graph[node][node + rows] = mat[i + 1][j]
    # add two 'fake' vertices that signify the start and end of the graph
    for i in range(rows):
        graph[0][rows * i + 1] = mat[i][0]
        graph[rows * i + columns][rows * columns + 1] = 0
    # assumes that all elements of mat do not exceed 4 digits
    distances = [9999 * (rows * columns)] * (rows * columns + 2)
    distances[0] = 0
    pq = [(0, 0)]
    # wanted to use PriorityQueue first, but you cannot update
    # the priority after it has been inserted in the queue (binary queue).
    # So this should suffice?
    while len(pq) > 0:
        current_distance, current_node = heapq.heappop(pq)
        for neighbour, cost in graph[current_node].items():
            alt_dist = current_distance + cost
            if alt_dist < distances[neighbour]:
                distances[neighbour] = alt_dist
                heapq.heappush(pq, (alt_dist, neighbour))
    return distances[-1]

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/081.txt", "r") as f:
        content = f.read()[:-1]
    mat = [list(map(int, row.split(','))) for row in content.split('\n')]
    print(problem(mat))
