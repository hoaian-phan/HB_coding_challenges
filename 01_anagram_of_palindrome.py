""" Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards (eg, “racecar”, “tacocat”). An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).

Determine if the given word is a re-scrambling of a palindrome.

The word will only contain lowercase letters, a-z."""

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome? 
    
    >>> is_anagram_of_palindrome("")
    False
    >>> is_anagram_of_palindrome("a")
    True
    >>> is_anagram_of_palindrome("ab")
    False
    >>> is_anagram_of_palindrome("aab")
    True
    >>> is_anagram_of_palindrome("arceace")
    True
    >>> is_anagram_of_palindrome("arceaceb")
    False
    
    """
    # if empty string -> False
    # make a dictionary of {char: occurrences}
    # counter to keep track of odd occurrences
    # iterate through the values of dictionary, count the odd values
    # if there are > 1 odd values, it's not a palindrome -> False
    # return True at the end of the loop

    if word == "":
        return False
    words = {}
    odd_counter = 0
    for char in word:
        words[char] = words.get(char, 0) + 1
    
    for value in words.values():
        if value % 2 != 0:
            odd_counter += 1
        
    if odd_counter > 1:
        return False
    
    return True


# Runtime: O(n)
# Spacetime: O(n)

# Running doctest
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)