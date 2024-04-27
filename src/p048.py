def problem():
    '''
        Returns last 10 digits of sum of powers. Wont bother too much with this,
        problem certainly shows its age.
    '''
    return str(sum(k ** k for k in range(1, 1000)))[-10:]

if __name__ == "__main__":
    print(problem())
