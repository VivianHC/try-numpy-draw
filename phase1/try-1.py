# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.9.17

# Description:
#   练习一维数组的创建
# ------------------------(max to 80 columns)-----------------------------------


import numpy as np
# ------------- 直接创建一维数组  nparray -------------------
print('----- 直接创建一维数组 cutting line -----')
# 默认为浮点数 - 常用于初始化
x = np.zeros(5)
print(x)

# 设置类型为整数 - 常用于初始化
y = np.zeros((5,), dtype=np.int)
print(y)
# ------------- 将列表或元组转化为一维数组  nparray -------------------
print('----- 将列表或元组转化为一维数组 cutting line -----')
# 从已有列表创建 np 数组
x = [1, 2, 3]
a = np.asarray(x)
print(a)

# 将元组转换为 ndarray:
x = (1, 2, 3)
a = np.asarray(x)
print(a)
# 设置了起始值、终止值及步长：
x = np.arange(10, 20, 2)
print(x)

x = np.arange(50, 30, -2)
print(x)
print('----- 设置等差数列 cutting line -----')
# 设置起始点为 1 ，终止点为 10，数列个数为 19或20
a = np.linspace(1, 10, 19)
print(a)
# 设置元素全部是1的等差数列：
a = np.linspace(1, 10, 10)
print(a)

# 将 endpoint 设为 false，不包含终止值：
a = np.linspace(10, 20,  5, endpoint=False)
print(a)
print('----- 设置等比数列 cutting line -----')
# 默认底数是 10
a = np.logspace(1.0,  2.0, num=10)
print(a)
# 将对数的底数设置为 2 :
a = np.logspace(0, 9, num=10, base=2)
print(a)
