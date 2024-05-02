def problem():
    '''
        Returns the sum of all 0-9 pandigital numbers n such that
        n has the substring divisibility property. Can be done by hand:

        Write the number as a0a1a2a3a4a5a6a7a8a9. Then it is easy to see that
        a5 = 5 since its substring a3a4a5 has to be divisible by 5 hence a5 = 5 or 0.
        If a5 = 0, then 0a6a7 has to be divisible by 11, which cannot happen. There are then
        only 8 multiples of 11 inside 500-599 without repeating digits:

            506, 517, 528, 539, 561, 572, 583, 594.

        We can check for each of these for a substring divisible by 13:
            528 6
            539 0
            572 8
            583 2
        
        We then check if 86x, 90x, 28x and 32x give rise to any multiples of 17. 
        And for all but the last one we have a match:
            528 6 7
            539 0 1
            572 8 9
        Thus we have 3 possible combinations:
            xxxx952867
            xxxxx53901 (impossible)
            xxxx357289
        where second one is impossible since 553 is only option.

        Suppose we have the first number. We have four digits left, 0, 1, 3, 4.
        Since a1a2a3 should be divisible by 2, a3 should be 0 or 4. Easy to see that
        it should be 0 and that a0, a1 are 1 or 4. So
        
            4130952867, 1430952867.

        It we take the last number, then similarly a3 should be 0, 4 or 6. 4 is impossible
        while 0 or 6 lead to the following numbers

            4160357289, 1460357289, 1406357289, 4106357289.
    '''
    return 4130952867 + 1430952867 + 4160357289 + 1460357289 + 1406357289 + 4106357289

if __name__ == "__main__":
    print(problem())
