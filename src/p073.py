def problem(d):
    pivot = (1, 2)
    neighbour = (1, 3)
    loops = 0
    while pivot[1] + neighbour[1] <= d:
        loops += 1
        neighbour = (pivot[0] + neighbour[0], pivot[1] + neighbour[1])
    return neighbour, loops


if __name__ == "__main__":
    print(problem(13))
