
def problem():
    '''
        Return the largest 16-digit number which can fit into a magic 5-gon.

        Done by hand: If r denotes the sum of the columns, then 5r should be about
        10 + ... + 1 = 55. We however count 5 numbers double, these can be 
        at minimum 1, 2, 3, 4 and 5, and at maximum 6, 7, 8, 9 and 10. As such

            5r - (6 + 7 + 8 + 9 + 10) <= 55
            5r - (1 + 2 + 3 + 4 + 5) >= 55

        thus 14 <= r <= 18. In fact, 10 cannot be repeated as we only care about
        16-digit numbers. Thus the upper bound can be tightened to 17.

        Now, the number will be the largest if the external nodes are maximized.
        In other words, if the numbers inside the pentagon are small. Thus r should be
        as small as possible for the number to be as big as possible.

        The smallest sum possible is 14, while the highest starting number is 6.
        By computing all 3-partitions of 14, we find that 6 only occurs in the sum 6 + 5 + 3.
        We can then finish this magic 5-gon quite easily:

            6 5 3; 10 3 1; 9 1 4; 8 4 2; 7 2 5.

        Since 10 is the largest possible digit occuring in the magic 5-gon, this number
        is automatically the largest possible number from a magic 5-gon.
    '''
    return 6531031914842725

if __name__ == "__main__":
    print(problem())
