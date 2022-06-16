""" Write a function that takes in a string and a character limit (as an integer). It should print the contents of the string without going over the character limit and without breaking words."""

def fit_to_width(string, num):
    """ Print the string within the character limit and without breaking words.

    >>> fit_to_width('Hello, world! I love Python and Hackbright',
    ...              10)
    Hello,
    world! I
    love
    Python and
    Hackbright
    """

    # A word : is divided by whitespace
    # split the string to a list of words
    #["Hello,", "world!", "I", "love", "Python", "and", "Hackbright"]
    # create a str_to_print = ""
    # iterate through each word in the list using index
        # if len(str_to_print) + 1 + len(words[index]) <= 10
            # add space and word to str_to_print
        # else:
            # print str_to_print
            # reset str_to_print = the word
        # if len(words[index]) >= 10:
        # print the word

    words = string.split()
    
    str_to_print = words[0]
    for i in range(1, len(words)):
        if len(str_to_print) + 1 + len(words[i]) <= num:
            str_to_print += " " + words[i]
        else:
            print(str_to_print)
            str_to_print = words[i]
        if len(words[i]) >= num:
            print(words[i])

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)


                