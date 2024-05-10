from collections import defaultdict
from pathlib import Path


def problem(attempts):
    '''
        Attempts to derive the shortest possible passcode from the given attempts.
        Assumes that every attempt is always asked in order.

        By hand/some basic computations:

        First create a graph where a vertex a is connected to b if a comes
        before b in some attempt. We then see that 7 does not come after any number
        hence optimally 7 will be the first digit. Thus 7 can be removed from the graph.
        Repeating this until the graph has no more edges:
            remove in order: 3,1,6,2,8,9 and finally 0.
        Problem: this only works if there are no repeating digits.
                Or rather: if every character in the passcode is unique.
    '''
    dependency_graph = defaultdict(set)
    options = set()
    for num in attempts:
        options.update(*(k for k in str(num)))
        dependency_graph[num[1]].add(num[0])
        dependency_graph[num[2]].add(num[1])
        dependency_graph[num[2]].add(num[0])
    sol = ''
    options = sorted(options)
    while options:
        temp = options.copy()
        for k in temp:
            if dependency_graph[k] == set():
                sol += k
                for d in dependency_graph:
                    dependency_graph[d] -= set(k)
                options.remove(k)
                break
        else:
            return 'SMTH WRONG'
    return sol

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/079.txt", "r") as f:
        contents = f.read()[:-1].split('\n')
    print(problem(contents[:]))
