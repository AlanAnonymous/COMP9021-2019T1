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



def Check(line, column, m, n):
	for a in range(line - n, line + n + 1):
		for b in range(column - m, column + m + 1):
			if not (0 <= a < len(grid) and 0 <= b < len(grid) and grid[a][b]):
				return False
	return True


def Modify(k):
	return (k > 0 and k + 1) or (k < 0 and k - 1) or (k == 0 and k)


def size_of_largest_isosceles_triangle():
	size, L = 0, [(-1, 0), (1, 0), (0, -1), (0, 1)]
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i][j]:
				for (m, n) in L:
					temp_size = 1
					while Check(i + m, j + n, abs(m), abs(n)):
						temp_size += 1
						m, n = Modify(m), Modify(n)
					size = max(size, temp_size)
	return size



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
