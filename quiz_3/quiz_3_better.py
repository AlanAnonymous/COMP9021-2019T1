# Written by Eric Martin for COMP9021



import sys
from random import seed, randint, randrange


try:
    arg_for_seed, upper_bound, length =\
            (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def length_of_longest_increasing_sequence(L):
    # pass
    # REPLACE pass ABOVE WITH  YOUR CODE

    LL, the_max, count = L + L, 0, 1
    for i in range(len(LL) - 1):
      if LL[i] <= LL[i + 1]:
        count += 1
      if (LL[i] > LL[i + 1]) or (i + 1 == len(LL) - 1):
        the_max = max(the_max, count)
        count = 1
    return min(the_max, len(L))


def max_int_jumping_in(L):
    # pass
    # REPLACE pass ABOVE WITH  YOUR CODE

    # 优化下算法，原理相同
    final_list = []
    for i in range(len(L)):
      visited, subList = [i], [L[i]]
      while subList[-1] not in visited:
        visited.append(subList[-1])
        subList.append(L[subList[-1]])
      if len(final_list) < len(subList):
        final_list = subList

    return int(''.join(str(k) for k in final_list))



seed(arg_for_seed)
L_1 = [randint(0, upper_bound) for _ in range(length)]
print('L_1 is:', L_1)
print('The length of the longest increasing sequence\n'
      '  of members of L_1, possibly wrapping around, is:',
      length_of_longest_increasing_sequence(L_1), end = '.\n\n'
     )
L_2 = [randrange(length) for _ in range(length)]
print('L_2 is:', L_2)
print('The maximum integer built from L_2 by jumping\n'
      '  as directed by its members, from some starting member\n'
      '  and not using any member more than once, is:',
      max_int_jumping_in(L_2)
     )


