# Written by *** and Eric Martin for COMP9021


'''
See https://en.wikipedia.org/wiki/Deterministic_finite_automaton

We consider as alphabet a set of digits.

We accept partial transition functions (that is, there might be no transition
for a given state and symbol).

With the accepts() function, we will deal with a single accept state rather than
a set of accept states.

In the test cases below, transitions_2 is the wikipedia example
(with 'S1' and 'S2' renamed as 'state_1' and 'state_2', respectively),
so the automaton that with 'state_1' as both initial and unique accept state,
accepts words with an even number of occurrences of 0's.

'''


def describe_automaton(transitions):
    '''
    The output is produced with the print() function.
    
    >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'}
    >>> describe_automaton(transitions_1)
    When in state "q0" and processing "0", automaton's state becomes "q1".
    When in state "q1" and processing "1", automaton's state becomes "q0".

    >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
                         ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    >>> describe_automaton(transitions_2)
    When in state "state_1" and processing "0", automaton's state becomes "state_2".
    When in state "state_1" and processing "1", automaton's state becomes "state_1".
    When in state "state_2" and processing "0", automaton's state becomes "state_1".
    When in state "state_2" and processing "1", automaton's state becomes "state_2".
    '''
##    pass
    # REPLACE pass ABOVE WITH YOUR CODE
    if transitions:
        # 遍历字典打印
        # \" 意思是是打印引号，其中 \ 是转义符
        for (state, digit) in transitions:
            print(f"When in state \"{state}\" and processing \"{digit}\", automaton's state becomes \"{transitions[(state, digit)]}\".")



def transitions_as_dict(transitions_as_list):
    '''
    transitions_as_list is a list of strings of the form 'state_1,symbol:state_2'
    where 'state_1' and 'state_2' are words and 'symbol' is one of the 10 digits.
    We assume that there is at most one 'state_2' for given 'state_1' and 'symbol'.
    
    >>> transitions_as_dict(['q0,0:q1', 'q1,1:q0'])
    {('q0', 0): 'q1', ('q1', 1): 'q0'}
    >>> transitions_as_dict(['state_1,0:state_2', 'state_1,1:state_1',\
                             'state_2,0:state_1', 'state_2,1:state_2'])
    {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', \
('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    '''
    transitions = {}
    # INSERT YOUR CODE HERE

    if transitions_as_list:
        # 遍历输入的list
        for i in range(len(transitions_as_list)):
            # 分割字符串  ' : '  (以冒号作为分隔符)
            NO_1_list = transitions_as_list[i].split(':')
            # NO_1_list[1]作为字典values已经符合输出要求，
            the_values = NO_1_list[1]
            # 但是， NO_1_list[0]作为字典keys还没有符合输出要求
            # 所以现在要对NO_1_list[0]进行操作，使之符号输出要求
            # 分割字符串  ' , '  (以逗号作为分隔符)
            NO_2_list = NO_1_list[0].split(',')
            the_keys = (NO_2_list[0], int(NO_2_list[1]))

            # 现在，完成了对transitions_as_list的一系列格式化操作，找出了keys和values
            # 添加入字典中
            transitions[the_keys] = the_values

    
    return transitions



def accepts(transitions, word, initial_state, accept_state):
    '''
    Starting in 'initial_state', if the automaton can process with 'transitions'
    all symbols in 'word' and eventually reach 'accept_state', then the function
    returns True; otherwise it returns False.
    
    >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'} 
    >>> accepts(transitions_1, '00', 'q0', 'q1')
    False
    >>> accepts(transitions_1, '2', 'q0', 'q0')
    False
    >>> accepts(transitions_1, '0101010', 'q0', 'q0')
    False
    >>> accepts(transitions_1, '01010101', 'q0', 'q0')
    True
    >>> not accepts(transitions_1, '01', 'q0', 'q1') and\
        accepts(transitions_1, '010', 'q0', 'q1')
    True

    >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
                         ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    >>> accepts(transitions_2, '011', 'state_1', 'state_1')
    False
    >>> accepts(transitions_2, '001110000', 'state_1', 'state_1')
    True
    >>> accepts(transitions_2, '1011100101', 'state_1', 'state_1')
    True
    >>> accepts(transitions_2, '10111000101', 'state_1', 'state_1')
    False
    '''
##    pass
    # REPLACE pass ABOVE WITH YOUR CODE

    # 去除掉一些特殊情况（可能有遗漏）
    if transitions == {} or word == '' or initial_state == '' or accept_state == '':
        return False

    # 找出最终状态final_state
    # 初始化final_state
    final_state = initial_state
    # 遍历字符串word
    for w in word:
        # 去除掉keys不在字典中的特殊情况(每次都要判断)
        if (final_state, int(w)) not in transitions:
            return False
        # final_state每次自动重置
        final_state = transitions[(final_state, int(w))]

    # 判断最终状态final_state和accept_state是否相等
    if final_state == accept_state:
        return True
    else:
        return False





    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
