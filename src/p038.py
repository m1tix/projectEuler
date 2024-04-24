def problem():
    '''
        Returns the largest 1-9 pandigital number that is a concatenated product
        of (1,2,..,n). This is done by hand: first digit must be a 9 by example
        given in question. Secondly, the multiplied number must be 4-digits or else
        the resulting concatenation is too short or too long. Hence it is of the form
            9xxx18xxx
        Second digit cannot be 5, 6 or 7 as that would exceed 19000. For same reason,
        cannot be 4. So second digit is either a 2 or a 3. If it is 3, one can check
        that the third digit cannot be a 6 or a 7 as the seventh digit is a 6
        or a 7. If the third digit is a 5 then there will always be a 0, impossible.
        If the third digit is a 4, then resulting number will not be pandigital.

        Thus third digit is a 2 and thus the seventh digit a 6. The largest possible
        answer is then 9327 which suprisingly creates a pandigital 1-9 number
        as a concatenated product with (1, 2)
    '''
    return '932718654'


if __name__ == "__main__":
    print(problem())
