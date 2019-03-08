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

    # 双倍的L，双倍的快乐
    # 初始化最大值和计数（计数是记录从每个i处开始一共有多少个满足条件的）
    LL, the_max, count = L + L, 0, 1
    # i+1 不能超范围
    for i in range(len(LL) - 1):
      # 判断条件1：<=，则count+=1
      if LL[i] <= LL[i + 1]:
        count += 1
      # 判断条件2：>，就停止count+=1，找出较大值，并重置count=1，也就是开始新的一轮判断
      # 然后防止list中前一个始终<=后一个的情况，使得程序不会进行第二个判断条件
      if (LL[i] > LL[i + 1]) or (i + 1 == len(LL) - 1):
        the_max = max(the_max, count)
        count = 1
    # 最后需要注意，the_max必须<=len(L)
    return min(the_max, len(L))


def max_int_jumping_in(L):
    # pass
    # REPLACE pass ABOVE WITH  YOUR CODE

    # List其实最后是[[1, 2, 5], [4, 2, 1]]这种形式
    List = []
    # 将所有的可能组合全部添加进入List中
    for i in range(len(L)):
      visited = [i]
      subList = [L[i]]
      while subList[-1] not in visited:
        visited.append(subList[-1])
        subList.append(L[subList[-1]])
      List.append(subList)

    # 从左向右，找出List中最长的那个元素(list类型)
    final_list = []
    for j in range(len(List)):
      if len(final_list) < len(List[j]):
        final_list = List[j]

    # 返回类型需要是int型
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


