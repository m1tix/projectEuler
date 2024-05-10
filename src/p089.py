from pathlib import Path

def problem(romans):
    '''
        Return the number of characters saved if we were to write the roman numerals
        in the list romans in minimal form.

    '''
    saved = 0
    i = 0
    max_index = len(romans) - 1
    while i < max_index - 1:
        if romans[i:i+5] in ('DCCCC', 'LXXXX', 'VIIII'):
            saved += 3
            i += 5
        elif romans[i:i+4] in ('CCCC', 'XXXX', 'IIII'):
            saved += 2
            i += 4
        else:
            i += 1
    return saved

if __name__ == "__main__":
    with open(Path(__file__).parent / "input/089.txt", "r") as f:
        content = f.read()
    print(problem(content))
