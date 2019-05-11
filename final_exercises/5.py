# You might find the ord() function useful.

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.
    
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''

    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    
    longest_string, string = '', word[0] if word else ''
    for w in word:
        if ord(string[-1]) + 1 == ord(w):
            string += w
        else:
            longest_string, string = string if len(longest_string) < len(string) else longest_string, w
    return string if len(longest_string) < len(string) else longest_string



if __name__ == '__main__':
    import doctest
    doctest.testmod()
