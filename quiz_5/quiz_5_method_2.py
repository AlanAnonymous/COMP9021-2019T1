# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by *** and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()



def decode(encoded_set):
    binary_string, the_decoded_list = (bin(encoded_set)[2:])[::-1], []
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            if i % 2 == 0:
                the_decoded_list.append(i // 2)
            else:
                the_decoded_list.append(-(i + 1) // 2)
    return sorted(the_decoded_list)



def display_encoded_set(encoded_set):
    # 这里可以写成：
    print('{', end = '')
    print(', '.join(str(e) for e in decode(encoded_set)), end = '')
    print('}')



def code_derived_set(encoded_set):
    encoded_running_sum, the_encoded_list = 0, decode(encoded_set)
    for i in range(1, len(the_encoded_list)):
        the_encoded_list[i] = the_encoded_list[i-1] + the_encoded_list[i]
    
    # 将二进制转化为十进制的方法二：用 int(string, 2)
    # 所以，需要得到一个由0和1组成的string

    # 首先，将最终的二进制码的为1的index记录下来
    index_list = []
    for element in set(the_encoded_list):
        if element >= 0:
            index_list.append(element * 2)
        else:
            index_list.append(element * (-2) - 1)
    
    # 然后弄成由0和1组成的string
    string = ''
    # 范围的上界需要是index_list中的最大数加上1
    # 可以将这个string当成长度为max(index_list) + 1的一串0
    # 然后在这个由0组成的string的特定的位置的值改成1
    # 因为string中是不可以修改元素的值的，所以用下面这种加法形式
    for j in range(max(index_list) + 1):
        # 有的话填1，没有的话填0
        if j in index_list:
            string += '1'
        else:
            string += '0'
    # 取其反序，并用内置函数int(string, 2)将其转化为十进制
    encoded_running_sum = int(string[::-1], 2)

    return encoded_running_sum




print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
    
