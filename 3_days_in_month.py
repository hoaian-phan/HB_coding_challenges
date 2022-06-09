""" Given a string with a month and a year (separated by a space), return the number of days in that month.

Leap years are a bit tricky. A year is a leap year if and only if:

it is evenly divisible by 4

except if it is divisible by 100, in which case it isn’t

except if it is divisible by 400, in which case it is

So, for example, 1904 was a leap year. 1900 is divisible by 100, so it wasn’t. 2000 is divisible by 400, so it was."""

def is_leap_year(year):
    """ Return True if leap year, False otherwise.
    >>> is_leap_year(1904)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

def days_in_month(date):
    """How many days are there in a month?
    >>> days_in_month("02 2015")
    28
    >>> days_in_month("02 2000")
    29
    >>> days_in_month("06 2022")
    30
    >>> days_in_month("12 1915")
    31
    """
    # Split the string to a list of string
    # Create a 30 day month set = value of all months that have 30 days
    # Check if month is February
        # yes, check if leap year
            # yes -> return 29
            # else -> return 28
        # else, check if month is in set of months
            # yes -> return 30
            # else -> return 31

    date_list = date.split()
    month, year = int(date_list[0]), int(date_list[1])
    set_30_days_month = {4, 6, 9, 11}

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    if month in set_30_days_month:
        return 30
    else:
        return 31

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)  