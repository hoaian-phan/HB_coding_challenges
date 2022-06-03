""" A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.
"""

def decode(s):
    """Decode a string.
    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'
    
    """
    # create a decoded_str variable, num_skip is the number of letter to skip
    # iterate through each char in the input str by index
        # if char is digit 
            #  num_skip = int(char)
            # decoded_str += s[index + 1 + num_skip]
    # return decoded_str

    decoded_str = ""
    num_skip = 0
    for index, char in enumerate(s):
        if char.isdigit():
            num_skip = int(char)
            decoded_str += s[index + 1 + num_skip]
    return decoded_str


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
