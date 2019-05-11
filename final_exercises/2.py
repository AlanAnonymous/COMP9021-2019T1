 
def rearrange(L, from_first = True):
    '''
    Returns a new list consisting of:
    * in case "from_first" is True:
         L's first member if it exists, then
         L's last member if it exists, then
         L's second member if it exists, then
         L's second last member if it exists, then
         L's third member if it exists...
    * in case "from_first" is False:
         L's last member if it exists, then
         L's first member if it exists, then
         L's second last member if it exists, then
         L's second member if it exists, then
         L's third last member if it exists...
         
    >>> L = []
    >>> rearrange(L), L
    ([], [])
    >>> L = [10]
    >>> rearrange(L, False), L
    ([10], [10])
    >>> L = [10, 20]
    >>> rearrange(L), L
    ([10, 20], [10, 20])
    >>> L = [10, 20, 30]
    >>> rearrange(L), L
    ([10, 30, 20], [10, 20, 30])
    >>> L = [10, 20, 30, 40]
    >>> rearrange(L, False), L
    ([40, 10, 30, 20], [10, 20, 30, 40])
    >>> L = [10, 20, 30, 40, 50]
    >>> rearrange(L, False), L
    ([50, 10, 40, 20, 30], [10, 20, 30, 40, 50])
    >>> L = [10, 20, 30, 40, 50, 60]
    >>> rearrange(L), L
    ([10, 60, 20, 50, 30, 40], [10, 20, 30, 40, 50, 60])
    >>> L = [10, 20, 30, 40, 50, 60, 70]
    >>> rearrange(L), L
    ([10, 70, 20, 60, 30, 50, 40], [10, 20, 30, 40, 50, 60, 70])
    '''
    
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    
    length, rearrange_L, New_L = len(L), [], L[::] if from_first else L[::-1]
    divisor, remainder = divmod(length, 2)
    for i in range(divisor):
        rearrange_L.extend([New_L[i], New_L[length - 1 - i]])
    return rearrange_L + [New_L[divisor]] if remainder else rearrange_L



if __name__ == '__main__':
    import doctest
    doctest.testmod()
