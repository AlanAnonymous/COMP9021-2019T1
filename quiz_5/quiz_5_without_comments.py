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
    print('{' + ', '.join(str(element) for element in decode(encoded_set)) + '}')



def code_derived_set(encoded_set):
    encoded_running_sum, the_encoded_list = 0, decode(encoded_set)
    for i in range(1, len(the_encoded_list)):
        the_encoded_list[i] = the_encoded_list[i-1] + the_encoded_list[i]
    for element in set(the_encoded_list):
        if element >= 0:
            encoded_running_sum += 2 ** (element * 2)
        else:
            encoded_running_sum += 2 ** (-element * 2 - 1)
    return encoded_running_sum




print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
    
