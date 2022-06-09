""" Given an integer n, return a list containing n unique random numbers between 1-10, inclusive. (That is, do not repeat any numbers in the returned list.)

You can trust that this function will never be called with n < 0 or n > 10."""

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).
    >>> lucky_numbers(0)
    []
    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """

    # import randint from random module
    # if n == 0 -> return empty list
    # Create a set to store unique random numbers
    # Iterate through each num in range n
        # generate random_num from randint(1, 10)
        # add to the set
    # Return the list type of the set

    from random import randint
    if n == 0:
        return []
    random_set = set()
    while len(random_set) < n:
        random_num = randint(1, 10)
        random_set.add(random_num)
    return list(random_set)

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)