from p038 import problem

if __name__ == "__main__":
    # same problem as 18 :)
    trgl = []
    with open('input/067.txt', 'r') as f:
        for line in f:
            trgl.append([int(entry) for entry in line.split(' ')])
    print(problem(trgl))
