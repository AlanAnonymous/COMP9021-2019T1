# Randomly fills a grid with True and False, with width, height and density
# controlled by user input, and computes the number of all "good paths" that link
# a point of coordinates (x1, y1) to a point of coordinates (x2, y2)
# (x1 and x2 are horizontal coordinates, increasing from left to right,
# y1 and y2 are vertical coordinates, increasing from top to bottom,
# both starting from 0), that is:
# - paths that go through nothing but True values in the grid
# - paths that never go through a given point in the grid more than once;
# - paths that never keep the same direction (North, South, East, West) over
#   a distance greater than 2.
#
# Written by *** and Eric Martin for COMP9021


from collections import namedtuple
import numpy as np 
from random import seed, randrange
import sys


Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))

def valid(pt):
    return 0 <= pt.x < width and 0 <= pt.y < height



# 多说几句。
# 刚学完递归，但理解不了递归，也不会用递归来做题是很正常的，
# 需要花一定的时间好好地理解这种思想。
# 这里稍微解释下递归的套路，原理以及一些容易遇见的问题：
#   套路：
#     首先，必须设置一个递归出口！！！也就是base case，也就是结束条件
#     其次，进入递归步骤中
#   原理（简要）：
#     递归过程中，会不断地记录每次递归的状态，
#       在此题中体现为，每次递归，都会记录下结束条件和四个方向（也就是记录下4个if语句，以及base case）
#     然后，到了递归出口时，意味着结束，
#     此时，递归将不断地返回上一级，直到没有上一级可以返回为止（也就是到了开始递归的时候，最初的状态的时候）

# Q1. 为什么要写回溯：
#   递归只记录了其中的代码，并没有记录其中的grid的每个状态
#   所以，需要一个回溯将改掉那个元素的值给改回来

# Q2. 为什么要写base case：
#   因为用递归的话，程序它自己是不知道什么时候停止的, 
#   所以需要一个结束条件来告诉它：好了结束了，不要继续递归了

# Q3. 为什么要用递归，不用for或while：
#   理论上来说，所有的递归都可以写成for循环或while循环
#   要知道，递归就是栈，栈是完全可以用for循环写出
#   所以，它们本质上没有区别，想用哪种就用哪种
#   不过，
#     在不知道到底循环多少次的时候，用递归好写一点
#     比如在这个在迷宫中找一条路，我并不知道到底要走多少次才能到达出口
#     那么，用递归好写一点，而且，一般来说，递归写法看起来会非常简洁

# Q4. 用递归发现RecursionError: maximum recursion depth exceeded in comparison
#   这就是递归不好的地方了，递归深度是有限制的，大概1000左右（也就是栈的深度为1000左右）
#   所以，下面这种递归写法在某些情况下会爆栈
#   解决方法就是，自己用循环写个栈，或者可以试试修改默认的栈的深度
#     import sys   
#     sys.setrecursionlimit(100000)
#   不过对于这道题而言，并不需要考虑爆栈的情况，这仅仅是quiz而已，quiz的测试并不需要考虑那么多
#   若是assignment的话，需要考虑一下

# Q5. 为什么都是if，不写if, elif
#   if, elif的话，只能进入其中一个语句中执行，也就是只能走一个方向，当然是不可以的

# Q6. 那为什么可以写成
#     if base case:
#        ...
#     else:
#        if ...
#           ...
#   我个人觉得写成if base case.... else这种要好一点，
#   要么满足结束条件，要么不满足（好理解一点）
#   不满足结束条件就说明还可以继续走，那么就继续向四个方向走
#   当然，不写else也没关系，只要base case处于前面就行，因为需要首先判断要不要继续走



# OTHER FUNCTIONS here #
def Recursion(x_1, y_1, x_2, y_2, up = 0, down = 0, left = 0, right = 0, count = 0):
    grid[x_1][y_1] = False
    if x_1 == x_2 and y_1 == y_2:
        count += 1
    if 0 <= x_1 - 1 < height and grid[x_1 - 1][y_1] and up < 2:
        count = Recursion(x_1 - 1, y_1, x_2, y_2, up + 1, 0, 0, 0, count)
    if 0 <= x_1 + 1 < height and grid[x_1 + 1][y_1] and down < 2:
        count = Recursion(x_1 + 1, y_1, x_2, y_2, 0, down + 1, 0, 0, count)
    if 0 <= y_1 - 1 < width and grid[x_1][y_1 - 1] and left < 2:
        count = Recursion(x_1, y_1 - 1, x_2, y_2, 0, 0, left + 1, 0, count)
    if 0 <= y_1 + 1 < width and grid[x_1][y_1 + 1] and right < 2:
        count = Recursion(x_1, y_1 + 1, x_2, y_2, 0, 0, 0, right + 1, count)
    grid[x_1][y_1] = True
    return count



def nb_of_good_paths(pt_1, pt_2):
    return Recursion(pt_1.y, pt_1.x, pt_2.y, pt_2.x)






try:
    for_seed, density, height, width = (abs(int(i)) for i in
                                                  input('Enter four integers: ').split()
                                       )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not density:
    density = 1
seed(for_seed)
grid = np.array([randrange(density) > 0
                              for _ in range(height * width)
                ]
               ).reshape((height, width))
print('Here is the grid that has been generated:')
display_grid()
try:
    i1, j1, i2, j2 = (int(i) for i in input('Enter four integers: ').split())
    pt_1 = Point(i1, j1)
    pt_2 = Point(i2, j2)
    if not valid(pt_1) or not valid(pt_2):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('Will compute the number of good paths '
      f'from ({pt_1.x}, {pt_1.y}) to ({pt_2.x}, {pt_2.y})...'
     )
paths_nb = nb_of_good_paths(pt_1, pt_2)
if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')
