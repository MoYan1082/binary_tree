# encoding: utf-8
"""
This module provides access to binary tree visualization
"""
import turtle
import math
from common import TreeNode

''' 相关的数据 '''
DEGREE = []
DEEP = 0
HEIGHT = 60 * (3 ** 0.5)

''' 画布的设置 '''
Tree = turtle.Turtle()
W = turtle.Screen()
W.title("二叉树可视化")
# 隐藏画笔
Tree.hideturtle()
Tree.speed(20)
Tree.pensize(2)

# 圆的半径
r = 25


# 写数据
def value(begin_x, begin_y, val):
    val = str(val)
    Tree.penup()
    Tree.goto(begin_x, begin_y - 10)
    Tree.pendown()
    if len(val) > 2:
        val = val[0] + val[1] + "…"
    Tree.write(val, align="center", font=("Courier", 14, "bold"))

    # 复原操作
    Tree.penup()
    Tree.goto(begin_x, begin_y)
    Tree.pendown()
    pass


# 圆圈
def center(begin_x, begin_y):
    Tree.penup()
    Tree.goto(begin_x, begin_y - r)
    Tree.pendown()
    Tree.circle(r)

    Tree.penup()
    Tree.goto(begin_x, begin_y)
    Tree.pendown()


# 左子树
def left(begin_x, begin_y, degree):
    length = HEIGHT / math.cos((degree - 90) / 180 * math.pi)
    Tree.right(degree)
    Tree.penup()
    Tree.forward(r)
    Tree.pendown()
    Tree.forward(length - 2 * r)
    Tree.penup()
    Tree.forward(r)
    Tree.pendown()
    Tree.left(degree)
    # Tree.circle(20)
    temp_x, temp_y = Tree.pos()
    center(temp_x, temp_y)
    Tree.penup()
    Tree.goto(begin_x, begin_y)
    Tree.down()
    _x = begin_x - math.sin((degree - 90) / 180 * math.pi) * length
    _y = begin_y - math.cos((degree - 90) / 180 * math.pi) * length
    return _x, _y


# 右子树
def right(begin_x, begin_y, degree):
    length = HEIGHT / math.cos((-degree + 90) / 180 * math.pi)
    Tree.right(degree)
    Tree.penup()
    Tree.forward(r)
    Tree.pendown()
    Tree.forward(length - 2 * r)
    Tree.penup()
    Tree.forward(r)
    Tree.pendown()
    Tree.left(degree)
    # Tree.circle(r)
    temp_x, temp_y = Tree.pos()
    center(temp_x, temp_y)
    Tree.penup()
    Tree.goto(begin_x, begin_y)
    Tree.down()
    _x = math.sin((-degree + 90) / 180 * math.pi) * length + begin_x
    _y = -math.cos((-degree + 90) / 180 * math.pi) * length + begin_y
    return _x, _y


def main(x_, y_, root, deep_):
    # Tree.forward(100)
    Tree.penup()
    Tree.goto(x_, y_)
    Tree.pendown()
    # print('操作了一次递归')
    value(x_, y_, root.val)
    if root.left is not None:
        # 90 + DEGREE[0]
        _x, _y = left(x_, y_, 90 + DEGREE[deep_])
        main(_x, _y, root.left, deep_ + 1)

    Tree.penup()
    Tree.goto(x_, y_)
    Tree.pendown()

    if root.right is not None:
        # 90 - DEGREE[0]
        _x, _y = right(x_, y_, 90 - DEGREE[deep_])
        main(_x, _y, root.right, deep_ + 1)

    # 提起笔不移动
    # Tree.penup()
    # 移动到某个位置
    # Tree.goto(x, y + 20)

    # 居中
    # Tree.write("1", align="center", font=("Courier", 14, "bold"))


def draw(root, deep):
    DEEP = deep
    te = 15
    last = 0
    DEGREE.append(15)
    for i in range(DEEP - 2):
        a = math.atan((HEIGHT * math.tan(te / 180 * math.pi) + r + 6 + last) / HEIGHT) / math.pi * 180
        last = (HEIGHT * math.tan(te / 180 * math.pi) + r + 6 + last) / 2
        te = a
        DEGREE.append(a)
    DEGREE.reverse()
    # 初始位置的朝向是水平向右
    # left是逆时针
    # right是顺时针
    # 正中心是0, 0
    x = 0
    y = 300
    Tree.penup()
    Tree.goto(x, y)
    Tree.pendown()
    center(x, y)
    main(x, y, root, 0)
    W.exitonclick()

'''
if __name__ == '__main__':
    #随便整一个二叉树
    binary_tree = TreeNode(1)
    temp = TreeNode(2111)
    binary_tree.left = temp
    temp = TreeNode(3)
    binary_tree.right = temp
    temp = TreeNode(4)
    binary_tree.left.left = temp
    temp = TreeNode(5)
    binary_tree.left.right = temp
    temp = TreeNode(6)
    binary_tree.right.left = temp
    temp = TreeNode(7)
    binary_tree.right.right = temp
    temp = TreeNode(8)
    binary_tree.left.left.left = temp
    temp = TreeNode(9)
    binary_tree.left.left.right = temp
    temp = TreeNode(10)
    binary_tree.left.right.left = temp
    temp = TreeNode(11)
    binary_tree.left.right.right = temp
    temp = TreeNode(12)
    binary_tree.right.left.left = temp
    temp = TreeNode(13)
    binary_tree.right.left.right = temp
    
    draw(binary_tree, 4)
'''