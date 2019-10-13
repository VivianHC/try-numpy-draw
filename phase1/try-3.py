# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt  # 约定俗成的写法plt
import numpy as np
# Try 1 ----------------------------------------------------------
# try1 简单的正弦余弦图
# 设置起始数值，以及取样点数
'''
start = -np.pi
stop = np.pi
point_num = 1000
# 设置x值， -π to+π的256个值
x = np.linspace(start, stop, point_num, endpoint=True)
# 首先定义两个函数（正弦&余弦）
C = np.cos(x)
S = np.sin(x)
plt.plot(x, C)
plt.plot(x, S)

# 在ipython的交互环境中需要这句话才能显示出来
'''
start = 0
stop = 1
point_num = 10000
plt.show()
x = np. linspace(start, stop, point_num, endpoint=True)
a = 2
b = 50

y =(x* x)/(x+2)+(1-x)**2/(-x+2)
plt.plot(x, y)
title='min(y)=%0.2f'%y.min()
plt.title(title)
