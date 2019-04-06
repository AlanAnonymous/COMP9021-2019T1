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



# interesting mothod... no optimization
# lower time complexity than other method
# time complexity: O(n^2)


def size_of_largest_isosceles_triangle():
	length = len(grid)
	
	# up:
	#  * * * * *
	#    * * *
	#      *
	matrix = [[0 for _ in range(length)] for _ in range(length)]
	for i in range(0, length, 1):
		for j in range(0, length, 1):
			if grid[i][j]:
				matrix[i][j] = 1
				if (0 <= i - 1) and (0 <= j - 1) and (j + 1 < 10):
					matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
	size_up = max(element for line in matrix for element in line)

	# down:
	#      *
	#    * * *
	#  * * * * *
	matrix = [[0 for _ in range(length)] for _ in range(length)]
	for i in range(length - 1, - 1, -1):
		for j in range(length - 1, - 1, -1):
			if grid[i][j]:
				matrix[i][j] = 1
				if (i + 1 < 10) and (0 <= j - 1) and (j + 1 < 10):
					matrix[i][j] = 1 + min(matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1])
	size_down = max(element for line in matrix for element in line)

	# left:
	#  *
	#  * *
	#  * * *
	#  * *
	#  *
	matrix = [[0 for _ in range(length)] for _ in range(length)]
	for j in range(0, length, 1):
		for i in range(0, length, 1):
			if grid[i][j]:
				matrix[i][j] = 1
				if (0 <= j - 1) and (0 <= i - 1) and (i + 1 < 10):
					matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i][j-1], matrix[i+1][j-1])
	size_left = max(element for line in matrix for element in line)

	# right:
	#      *
	#    * *
	#  * * *
	#    * *
	#      *
	matrix = [[0 for _ in range(length)] for _ in range(length)]
	for j in range(length - 1, -1, -1):
		for i in range(length - 1, -1, -1):
			if grid[i][j]:
				matrix[i][j] = 1
				if (j + 1 < 10) and (0 <= i - 1) and (i + 1 < 10):
					matrix[i][j] = 1 + min(matrix[i-1][j+1], matrix[i][j+1], matrix[i+1][j+1])
	size_right = max(element for line in matrix for element in line)
	

	return max(size_up, size_down, size_left, size_right)
    



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
