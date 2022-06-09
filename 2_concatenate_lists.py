""" Given two lists. concatenate them (that is, combine them into a single list)."""

def concat_lists(list1, list2):
    """Combine lists.
    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> concat_lists([], [1, 2])
    [1, 2]
    >>> concat_lists([1, 2], [])
    [1, 2]
    >>> concat_lists([], [])
    []
    """

    return list1 + list2

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)