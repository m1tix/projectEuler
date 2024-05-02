from pathlib import Path
from itertools import product

def frequency_count(s):
    '''
        Return frequency count of each ASCII character in given list
    '''
    found_letters = dict()
    for t in s:
        try:
            found_letters[int(t)] += 1
        except KeyError:
            found_letters[int(t)] = 1
    return found_letters

def decode(crypt_text, key):
    '''
        Decode the given crypt text with the given key.
    '''
    res = ""
    for i in range(len(crypt_text)):
        res += chr(int(crypt_text[i]) ^ key[i % 3])
    return res

def problem(crypt_text):
    '''
        Crack the given cryptotext, which is known to be encrypted with XOR encryption,
        and return the sum of the ASCII characters.

        Observations:
            - Whitespaces, brackets, commas etc are included it seems.
            - The three most used letters in english language are e, t and a (see any frequency analysis)
    '''
    letters = crypt_text[:-1].split(',')
    possibilities = [[], [], []]
    for k in range(3):
        freq_letters = frequency_count(letters[k::3])
        most_freq_letter = max(freq_letters, key=lambda x: freq_letters[x])
        for c in [' ', 'e', 'E', 't', 'T', 'a', 'A']:
            if ord('a') <= most_freq_letter ^ ord(c) <= ord('z'):
                possibilities[k].append(most_freq_letter ^ ord(c))
    for key in product(*possibilities):
        res = decode(letters, key)
        print(''.join(res))
        print(sum(ord(c) for c in res))
    return None


if __name__ == "__main__":
    with open(Path(__file__).parent / 'input/059.txt', 'r') as f:
        cont = f.read()
    print(problem(cont))
