#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/15/2020 2:27 PM
# @Author : QH
# @Site : WUXI
# @File : 条形图的绘制方法.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置支持中文显示功能
plt.rcParams['axes.unicode_minus'] = False #设置支持显示负数功能
y = [12,15,11,8,12]
x = ['lili','lucy','john','mary','frank']
plt.bar(x,y,align='center',color = 'green')
plt.xlabel('姓名',labelpad=5,fontsize = 17)
plt.ylabel('销售额')
plt.title('不同人的销售量',pad=10)     #pad=10设置标签距离坐标轴的距离
# plt.grid(ls='--',c = 'darkblue')      #给图形设置网格线
plt.axhline(y=10,c= 'red',ls = '--',lw = 2)     #设置水平的横线
plt.axvline(x = 2,c = 'blue',ls = '--')      #设置垂直的竖线
plt.axvspan(3,4,facecolor = 'red')   # 在图形中绘制出垂直的横条


