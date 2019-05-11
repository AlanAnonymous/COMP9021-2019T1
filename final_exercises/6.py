# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    
    for h in range(height):
        string = ''
        for w in range(width):
            string += chr(97 + (h * width + w) % 26)
        print(string[::-1]) if h % 2 else print(string)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
