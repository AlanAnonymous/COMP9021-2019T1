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



###### DEFINE OTHER FUNCTIONS here: ######
# encode_set is the input number(int type)
def decode(encoded_set):
    # use 'bin()' to convert decimal to binary
    # '[2:]' means: get the number(string type) without '0b'
    # '[::-1]' means: reverse the string
    binary_string = (bin(encoded_set)[2:])[::-1]
    # initialize an empty list called the_decoded_list
    # the decoded number(integer type) should be added into it
    the_decoded_list = []
    # loop
    for i in range(len(binary_string)):
        # find the position(index) of '1'
        if binary_string[i] == '1':
            # if the index of this '1' is even
            if i % 2 == 0:
                # make some simple calculations
                the_decoded_list.append(i // 2)
            # else, the index of this '1' is odd
            else:
                # make some simple calculations
                the_decoded_list.append(-(i + 1) // 2)
    # ultimately, return the the_decoded_list which should be ascending order
    # the_decoded_list may be empty or not, but it doesn't matter
    return sorted(the_decoded_list)



# POSSIBLY DEFINE OTHER FUNCTIONS    
def display_encoded_set(encoded_set):
    # pass
    # REPLACE pass ABOVE WITH CODE TO PRINT OUT ENCODED SET (WITH print() STATEMENTS)

    # OTHER FUNCTIONS is written above
    decoded_list = decode(encoded_set)
    print('{' + ', '.join(str(element) for element in decoded_list) + '}')



def code_derived_set(encoded_set):
    encoded_running_sum = 0
    # REPLACE THIS COMMENT WITH YOUR CODE

    # utilise the function above to get the sorted(the_decoded_list)
    the_encoded_list = decode(encoded_set)
    # loop
    # change the elements which are in the_encoded_list
    # except the first element in the_encoded_list
    for i in range(1, len(the_encoded_list)):
        the_encoded_list[i] = the_encoded_list[i-1] + the_encoded_list[i]
    # remove duplicate elements in the_encoded_list
    the_set = set(the_encoded_list)
    # then loop
    # this loop is to convert binary to decimal
    for element in the_set:
        # if element >= 0
        if element >= 0:
            # make some simple calculations
            encoded_running_sum += 2 ** (element * 2)
        # else, element < 0
        else:
            # make some simple calculations
            encoded_running_sum += 2 ** (-element * 2 - 1)
    # return encoded_running_sum
    return encoded_running_sum



print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
    
