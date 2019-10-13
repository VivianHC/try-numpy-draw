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
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.gca(projection='3d')
start = -10
stop = 10
point_num = 970


x = np. linspace(start, stop, point_num, endpoint=False)
y=1-x
z =(x* x)/(x+2)+y**2/(y+1)
print(z.min())
ax.plot(x,y,z,label='parametric curve')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Lable')
print(z.min())
ax.legend()
plt.show()
