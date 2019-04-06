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

'''
因为这道题的grid就是10*10的大小，而且最终的size不会超过5
那么就有了下面这种暴力写法
完全不用费脑子的写法。。。。。。
只是有点费手。。。。。。
而且时间复杂度（最坏情况）为：O(n^3)

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
	
	(向下---down)
	第一行看：grid[i][j]
		若此位置的值不为0，则size = 1
	
	第二行看：grid[i+1][j-1], 
			  grid[i+1][j], 
			  grid[i+1][j+1]
		若都不为0，则size += 1
		否则，结束
	
	第三行看：grid[i+2][j-2], 
			  grid[i+2][j-1], 
			  grid[i+2][j], 
			  grid[i+2][j+1], 
			  grid[i+2][j+1]
		若都不为0，则size += 1
		否则，结束
	......


也就是(例子)：
      1			<--- 找到grid中的不为0的这个位置，也就是找到三角形的‘顶点’，其顶点的角度为90°（size为1）
   2  1  3		<--- 然后，看‘顶点’下面这行。看这行的3个点的值是否都不为0，发现都不为0，则继续看下一行（size+=1，size为2）
1  0  4  2  1	<--- 然后，看‘顶点’下面的下面这行。当遍历这行的时候，发现第二个位置的值为0，那么结束（size不变，仍为2）
注意：生成的grid中的数字为：0 到 density 这个范围，density是输入的第二个数字


虽然是这种写法很‘辣鸡’，花费的时间也很多
但是
‘不管黑猫白猫，能抓到老鼠的就是好猫’



优化写法请看：
'quiz_6_暴力解法_优化写法.py'

'''

def WithinRange(x, y, z):
	if 0 <= x < len(grid) and 0 <= y < len(grid) and 0 <= z < len(grid):
		return True
	else:
		return False


def size_of_largest_isosceles_triangle():
	size = 0
	for i in range(10):
		for j in range(10):
			if grid[i][j]:

				# up
				size_up = 1
				if (WithinRange(i-1, j-1, j+1) and grid[i-1][j-1] and grid[i-1][j] and grid[i-1][j+1]):
					size_up = 2
					
					if (WithinRange(i-2, j-2, j+2) and grid[i-2][j-2] and grid[i-2][j-1] and grid[i-2][j] 
					and grid[i-2][j+1] and grid[i-2][j+2]):
						size_up = 3
						
						if (WithinRange(i-3, j-3, j+3) and grid[i-3][j-3] and grid[i-3][j-2] and grid[i-3][j-1] 
						and grid[i-3][j] and grid[i-3][j+1] and grid[i-3][j+2] and grid[i-3][j+3]):
							size_up = 4

							if (WithinRange(i-4, j-4, j+4) and grid[i-4][j-4] and grid[i-4][j-3] and grid[i-4][j-2] and grid[i-4][j-1] 
							and grid[i-4][j] and grid[i-4][j+1] and grid[i-4][j+2] and grid[i-4][j+3] and grid[i-4][j+4]):
								size_up = 5

				# down
				size_down = 1
				if (WithinRange(i+1, j-1, j+1) and grid[i+1][j-1] and grid[i+1][j] and grid[i+1][j+1]):
					size_down = 2
					
					if (WithinRange(i+2, j-2, j+2) and grid[i+2][j-2] and grid[i+2][j-1] and grid[i+2][j] 
					and grid[i+2][j+1] and grid[i+2][j+2]):
						size_down = 3
						
						if (WithinRange(i+3, j-3, j+3) and grid[i+3][j-3] and grid[i+3][j-2] and grid[i+3][j-1] 
						and grid[i+3][j] and grid[i+3][j+1] and grid[i+3][j+2] and grid[i+3][j+3]):
							size_down = 4

							if (WithinRange(i+4, j-4, j+4) and grid[i+4][j-4] and grid[i+4][j-3] and grid[i+4][j-2] and grid[i+4][j-1] 
							and grid[i+4][j] and grid[i+4][j+1] and grid[i+4][j+2] and grid[i+4][j+3] and grid[i+4][j+4]):
								size_down = 5

				# left
				size_left = 1
				if (WithinRange(i-1, i+1, j-1) and grid[i-1][j-1] and grid[i][j-1] and grid[i+1][j-1]):
					size_left = 2
					
					if (WithinRange(i-2, i+2, j-2) and grid[i-2][j-2] and grid[i-1][j-2] and grid[i][j-2] 
					and grid[i+1][j-2] and grid[i+2][j-2]):
						size_left = 3
						
						if (WithinRange(i-3, i+3, j-3) and grid[i-3][j-3] and grid[i-2][j-3] and grid[i-1][j-3] 
						and grid[i][j-3] and grid[i+1][j-3] and grid[i+2][j-3] and grid[i+3][j-3]):
							size_left = 4

							if (WithinRange(i-4, i+4, j-4) and grid[i-4][j-4] and grid[i-3][j-4] and grid[i-2][j-4] and grid[i-1][j-4] 
							and grid[i][j-4] and grid[i+1][j-4] and grid[i+2][j-4] and grid[i+3][j-4] and grid[i+4][j-4]):
								size_left = 5
				
				# right
				size_right = 1
				if (WithinRange(i-1, i+1, j+1) and grid[i-1][j+1] and grid[i][j+1] and grid[i+1][j+1]):
					size_right = 2
					
					if (WithinRange(i-2, i+2, j+2) and grid[i-2][j+2] and grid[i-1][j+2] and grid[i][j+2] 
					and grid[i+1][j+2] and grid[i+2][j+2]):
						size_right = 3
						
						if (WithinRange(i-3, i+3, j+3) and grid[i-3][j+3] and grid[i-2][j+3] and grid[i-1][j+3] 
						and grid[i][j+3] and grid[i+1][j+3] and grid[i+2][j+3] and grid[i+3][j+3]):
							size_right = 4

							if (WithinRange(i-4, i+4, j+4) and grid[i-4][j+4] and grid[i-3][j+4] and grid[i-2][j+4] and grid[i-1][j+4] 
							and grid[i][j+4] and grid[i+1][j+4] and grid[i+2][j+4] and grid[i+3][j+4] and grid[i+4][j+4]):
								size_right = 5

				size = max(size, size_up, size_down, size_left, size_right)
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
