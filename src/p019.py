from math import floor


def problem(begin_date, end_date):
    '''
        Returns the number of sundays between beginDate and endDate that fell
        on the first of the month (where the year of beginDate is bigger than
        1900).
        The dates are formatted as a list [Y, M, D] where Y denotes the year, M
        the month and D the day (as integers).

        Uses Gauss's algorithm (could not get Zeller's to work), see
            https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    '''
    gauss_value = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    count = 0
    current_year, current_month = begin_date[:2]
    end_year, end_month = end_date[:2]
    if begin_date[2] != 1:
        current_month += 1
        if current_month == 13:
            current_year += 1
            current_month = 1
    L = (end_year - current_year) * 12 + end_month - current_month + 1
    for _ in range(L):
        g = gauss_value[current_month - 1]
        if current_month in (1, 2):
            Y = current_year - 1
        else:
            Y = current_year
        y = Y % 100
        c = Y // 100
        h = (1 + g + y + floor(y / 4) + floor(c / 4) - 2 * c) % 7
        if h == 0:
            count += 1
        current_month += 1
        if current_month == 13:
            current_month = 1
            current_year += 1

    return count


if __name__ == "__main__":
    print(problem([1901, 1, 1], [2000, 12, 31]))
