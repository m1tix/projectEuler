from problem018 import problem018
if __name__ == "__main__":
    # same problem as 18 :)
    trgl = []
    with open('Inputs/problem067.txt', 'r') as f:
        for line in f:
            trgl.append([int(entry) for entry in line.split(' ')])
    print(problem018(trgl))
