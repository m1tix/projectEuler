from math import floor


def problem019(beginDate, endDate):
    '''
        Returns the number of sundays between beginDate and endDate that fell
        on the first of the month (where the year of beginDate is bigger than
        1900).
        The dates are formatted as a list [Y, M, D] where Y denotes the year, M
        the month and D the day (as integers).

        Uses Gauss's algorithm (could not get Zeller's to work), see
            https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    '''
    gaussValue = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    count = 0
    currentYear, currentMonth = beginDate[:2]
    endYear, endMonth = endDate[:2]
    if beginDate[2] != 1:
        currentMonth += 1
        if currentMonth == 13:
            currentYear += 1
            currentMonth = 1
    L = (endYear - currentYear) * 12 + endMonth - currentMonth + 1
    for _ in range(L):
        g = gaussValue[currentMonth - 1]
        if currentMonth in (1, 2):
            Y = currentYear - 1
        else:
            Y = currentYear
        y = Y % 100
        c = Y // 100
        h = (1 + g + y + floor(y / 4) + floor(c / 4) - 2 * c) % 7
        if h == 0:
            count += 1
        currentMonth += 1
        if currentMonth == 13:
            currentMonth = 1
            currentYear += 1

    return count


if __name__ == "__main__":
    print(problem019([1901, 1, 1], [2000, 12, 31]))
