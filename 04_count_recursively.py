""" Count the number of items in a list, using recursion."""

def count_recursively(lst):
    """Return number of items in a list, using recursion.
    >>> count_recursively([])
    0
    >>> count_recursively([1])
    1
    >>> count_recursively([1, 2, 3])
    3
    >>> count_recursively([1, 2, 3, 6, 3, 7, 2, 10])
    8
    """

    # base case: [] -> 0, [1] -> 1
    # regular case: return 1 + call recursive function on [1:]

    if lst == []:
        return 0

    if len(lst) == 1:
        return 1

    return 1 + count_recursively(lst[1:])

    # Running doctest
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)