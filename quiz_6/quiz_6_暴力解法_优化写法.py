# Randomly generates a grid with 0s and 1s, whose 10ension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


# 简化后的代码如下：(虽然不是暴力写法，但是仍然是暴力解法)
# time complexity(worst case): O(n^3)

# up:
#  * * * * *
#    * * *
#      *

# down:
#      *
#    * * *
#  * * * * *

# left:
#  *
#  * *
#  * * *
#  * *
#  *

# right:
#      *
#    * *
#  * * *
#    * *
#      *


### OTHER FUNCTION 1 ###
def Check(line, column, m, n):
	# one of m and n is 0
	for a in range(line - n, line + n + 1):
		for b in range(column - m, column + m + 1):
			# if a out of range, return False
			# then, if b out of range, return False
			# after that, if grid[a][b] == 0, return False
			if not (0 <= a < len(grid) and 0 <= b < len(grid) and grid[a][b]):
				return False
	# if all elements of this line/column in grid are equal to 1, return True
	return True


### OTHER FUNCTION 2 ###
def Modify(k):
	# if k > 0, then k += 1
	# else if k < 0, then k -= 1
	# else(k == 0), do nothing about it
	# (Martin said the principlef of the code below in lecture)
	return (k > 0 and k + 1) or (k < 0 and k - 1) or (k == 0 and k)


### original FUNCTION ###
# find the position of apex of triangle, then, 'check' next line/column
# i.e.
# 	1	<---- find this point
# 2 0 3	<---- then, 'check' next line
def size_of_largest_isosceles_triangle():
    # pass
    # REPLACE pass WITH YOUR CODE
	
	size = 0
	# up, down, left, right
	L = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i][j]:
				for (m, n) in L:
					# initialize/reset temp_size before 'while'
					temp_size = 1
					# check whether all elements of this line/column are not equal to 0
					while Check(i + m, j + n, abs(m), abs(n)):
						# if so, increase temp_size by 1
						temp_size += 1
						# then, check next line/column
						m, n = Modify(m), Modify(n)
					size = max(size, temp_size)
	return size

# POSSIBLY DEFINE OTHER FUNCTIONS


try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
     )
