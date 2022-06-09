""" Given list of ints, return True if any two nums in list sum to 0. """

def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.
    >>> add_to_zero([])
    False
    >>> add_to_zero([1])
    False
    >>> add_to_zero([1, 2, 3])
    False
    >>> add_to_zero([1, 2, 3, -2])
    True
    >>> add_to_zero([0, 1, 2])
    True
    """
    # if the list has < 2 elements -> return False
    # Create a set from the list nums
    # Iterate through the nums list
        # if 0 in the set, return True
        # if - num in the set, return True
    # Return False

    if len(nums) < 2:
        return False
    nums_set = set(nums)
    for num in nums:
        if num == 0:
            return True
        if -num in nums_set:
            return True
    return False

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
