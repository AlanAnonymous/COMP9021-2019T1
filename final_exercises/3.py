
def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).
    You can assume that "number" is an integer at least equal to 2.
    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE

    N, Set, Product = number, set(), 1

    while N % 2 == 0:
        Set.add(2)
        N //= 2
    
    for d in range(3, number + 1, 2):
        while N % d == 0:
            Set.add(d)
            N //= d
        if N == 1:
            break
    
    for S in Set:
        Product *= S
    
    return Product



if __name__ == '__main__':
    import doctest
    doctest.testmod()
