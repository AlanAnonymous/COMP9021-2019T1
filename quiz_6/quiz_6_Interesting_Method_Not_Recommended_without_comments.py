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



# time complexity: O(n^2)
def size_of_largest_isosceles_triangle():
    length, size, new_grid = len(grid), 0, [row[:] for row in grid]
    for _ in range(4):
        new_grid = list(list(x)[::-1] for x in zip(*new_grid))
        matrix = [[0 for _ in range(length + 2)] for _ in range(length + 1)]
        for i in range(length):
            for j in range(length):
                if new_grid[i][j]:
                    matrix[i+1][j+1] = 1 + min(matrix[i][j], matrix[i][j+1], matrix[i][j+2])
                    size = max(size, max(element for line in matrix for element in line))
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
