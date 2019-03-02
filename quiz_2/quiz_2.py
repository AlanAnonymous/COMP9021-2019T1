# Written by *** and Eric Martin for COMP9021


def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}

def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    # INSERT YOUR CODE HERE TO PRINT 4 LINES

    # 遍历字典打印
    if rule:
        for (x, y), z in rule.items():
            print(f"After {x} followed by {y}, we draw {z}")


#############################################################
# 自行添加的函数
# 获取字符串
def get_string(rule_nb, first, second, length):
    # 字典
    rule = rule_encoded_by(rule_nb)
    # 初始化string
    string = ''
    if length > 0:
        if length == 1:
            string += str(first)
        else:
            string += str(first) + str(second)
            # v是变量
            v = 0
             # 按照一定规律循环添加数据
            for _ in range(length - 2):
                string += str(rule[(int(string[v]), int(string[v+1]))])
                v += 1
    # 返回这个字符串
    return string
#############################################################



def draw_line(rule_nb, first, second, length):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    
    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    # rule = rule_encoded_by(rule_nb)
    # INSERT YOUR CODE HERE TO PRINT ONE LINE

    # 打印
    print(get_string(rule_nb, first, second, length))




def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
    # pass
    # REPLACE pass ABOVE WITH YOUR CODE
    
    # 穷举法：
    # 已知三个变量 first, second, length，剩余一个变量 rule_nb
    # 而 rule_nb 共16种情况(0-15)，所以共要尝试16次

    # count用来计数，作用是看是否唯一
    count = 0
    length = len(line)
    # 其实length<=1，count肯定不唯一，所以并不需要看length<=1的情况
    # 因此，下面的条件中是只需要判断length>=2的情况就行
    if length >= 2:
        # 每次循环得出字符串都要与line对比
        for rule_nb in range(16):
             string = get_string(rule_nb, line[0], line[1], length)
             # 如果相等，就说明找到规则了
             if line == string:
                 # 计算count的值
                 count += 1
                 # 记录rule_nb
                 result = rule_nb

    # 检查是否唯一
    if count == 1:
        return result
    # 不唯一就返回-1
    else:
        return -1


