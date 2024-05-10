import heapq
from pathlib import Path
from collections import defaultdict


def problem(mat):
    '''
        Returns the minimal path sum starting from the top left corner to the bottom
        right corner and by moving in any direction.

        Same setup as p082 and p081, but even harder! Yet our solution in p082 should suffice
    '''
    rows = len(mat)
    columns = len(mat[0])
    graph = defaultdict(dict)
    # first construct graph
    for i in range(rows):
        for j in range(columns):
            node = rows * i + j
            if j != columns - 1:
                # right neighbour exists
                graph[node][node + 1] = mat[i][j+1]
            if j != 0:
                # left neighbour exists
                graph[node][node - 1] = mat[i][j - 1]
            if i != 0:
                # upper neighbour exists
                graph[node][node - rows] = mat[i - 1][j]
            if i != rows - 1:
                # down neighbour exists
                graph[node][node + rows] = mat[i + 1][j]
    distances = [99999 * (rows * columns)] * (rows * columns)
    distances[0] = mat[0][0]
    pq = [(mat[0][0], 0)]
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
