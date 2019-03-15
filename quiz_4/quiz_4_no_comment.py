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

with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    # pass
    # REPLACE pass above WITH YOUR CODE
    
    next(file)
    List = []
    for line in file:
        if line and line[2] == indicator_of_interest:
            for i in range(4, number_of_years + 4):
                if line[i]:
                    float_line_i = float(line[i])
                    List.append([line[0], i - 4 + first_year, float_line_i])
                    if max_value is None:
                        max_value = float_line_i
                    else:
                        if max_value < float_line_i:
                            max_value = float_line_i


if max_value is not None:
    for [Countries, Years, Value] in List:
        if Value == max_value:
            if Years not in countries_for_max_value_per_year:
                countries_for_max_value_per_year[Years] = [Countries]
            else:
                countries_for_max_value_per_year[Years].append(Countries)


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
