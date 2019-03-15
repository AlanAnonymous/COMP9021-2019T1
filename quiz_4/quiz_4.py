# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
#
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import gzip


filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}


'''
此题思路：
    第1步：读取csv文件，找出第3列数据与输入的indicator_of_interest一样的那些行
    第2步：将这些行中的countrie, year, value这些数据用一个list记录下来（用字典也可以）
    第3步：顺带找出max_value的值
    
    第4步：建立字典，也就是将这个value等于max_value的元素中的year作为字典的keys，countrie作为字典的values
    
    第5步：根据题目要求，输出的max_value可能是整型，也可能是float型，所以需要修正max_value
    第6步：根据题目要求，字典应该根据年份排序，不过输出代码中已经写好，所以不需要进行此步骤
'''


# 第1，2，3步：
with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    # pass
    # REPLACE pass above WITH YOUR CODE

    # 不看第一行，也就是从第二行开始读取数据
    next(file)

    # List是一个为空的list
    List = []

    # 读取每行数据
    for line in file:
        # 首先要保证这行存在
        # 然后看这一行的第3列数据与输入的indicator_of_interest是否匹配
        # 匹配的话就说明找到了对应的位置了
        if line and line[2] == indicator_of_interest:
            # 由题意，要在56(number_of_years)个数据中找出最大值
            # 这56个数据(value)都是在年份下面的，它们都是从第5列开始的
            for i in range(4, number_of_years + 4):
                # 此行的此列有数据才继续(line[i]代表当前这一行的第i列)
                if line[i]:
                    # csv文件的的数据几乎都是浮点型（少量整型），但是读取数据的时候是字符型，所以需要将str型转化为float型
                    # 并且，转化为float型比较数据的大小才不会出错
                    float_line_i = float(line[i])
                    # 先将国家，年份（年份需要稍微计算一下），value(float型)都记录下来
                    List.append([line[0], i - 4 + first_year, float_line_i])
                    # 然后，需要找出max_value，下面是max_value的两种情况，为None和不为None
                    # line[i]存在，且max_value为None
                    if max_value is None:
                        # 则将max_value替换为line[i]
                        max_value = float_line_i
                    # 否则，line[i]存在，但max_value不为None，也就是max_value存在
                    else:
                        # 那么比较两个浮点型数据的大小
                        # 若max_value不是最大，将其替换。否则不变
                        if max_value < float_line_i:
                            max_value = float_line_i


# 第4步：
# 至此，遍历此文件的循环结束，文件关闭，并且生成了装有一些数据的List
# 然后就需要挑选出List中元素中的value等于max_value的元素，并建立字典
# 首先要排除掉max_value是None的情况
if max_value is not None:
    # 从List中取出元素（每个元素中都包含3个变量）
    for [Countries, Years, Value] in List:
        # 判断两个float型的数是否相等（注意：这里是可以用 == 比较的）
        if Value == max_value:
            # Value等于max_value的话，就说明当前元素是需要被添加进字典中的
            # 下面就是将特定数据添加进字典的操作（比较容易理解的一种写法）
            # 不存在就新建，存在就在此基础上添加
            if Years not in countries_for_max_value_per_year:
                countries_for_max_value_per_year[Years] = [Countries]
            else:
                countries_for_max_value_per_year[Years].append(Countries)


# 第5步：
# 最后，修正max_value的值，其实就是让100.0变成100，49.4这种不变
# 当然也可以说：int型保持为int型，float型保持为float型
if max_value is not None:
    if max_value % 1 == 0:
        max_value = int(max_value)


if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )
