""" Binary search is one of the most important Computer Science algorithms. It allows you to search a sorted list in O(log n) time, a large improvement over scanning every item in the list (which would be O(n) time).

To do this, you examine the middle item and, if the sought-for value is smaller, move halfway to the left. If the sought-after value is larger, move halfway to the right.

In this challenge, you’ll make binary search for the classic children’s guessing game of “pick a number from 1 to 100”.

Since you use binary search, it will never take more than 7 guesses for a function to find a number in the range 1 to 100 (since log2 100) is just a little under 7)."""

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.
    >>> binary_search(50)
    1
    >>> binary_search(25)
    2
    >>> binary_search(75)
    2
    >>> binary_search(31) <= 7
    True
    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """

    # create start = 1 and end = 100 variable
    # use num_guesses to keep track of number of guesses
    # first guess = (start + end) // 2 -> increment num_guesses by 1
    # while loop while guess != val
        # if guess is larger than val -> move end to the left of guess
        # else -> move start to the right of guess
        # recalculate guess = (start + end) // 2
        # increment num_guesses
    # return num_guesses

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0
    start = 1
    end = 100
    # Make the first guess
    guess = (start + end) // 2
    num_guesses += 1

    # While not guessing the right answer
    while guess != val:
        if guess > val:
            end = guess - 1
        elif guess < val:
            start = guess + 1
        guess = (start + end) // 2
        num_guesses += 1

    return num_guesses


    # Running doctest
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)