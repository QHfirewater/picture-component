#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/15/2020 4:03 PM
# @Author : QH
# @Site : WUXI
# @File : 堆叠图绘制.py
# @Software: PyCharm
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置支持中文显示功能
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel(r'E:\公司文档\自动化\New folder\测试数据1.xls')
df2 = df.iloc[:5,:]
plt.bar(x = df2['时间'],height = df2['SO2'],label = 'SO2',tick_label = ['1日','2日','3日','4日','5日']) #设置第一个图
plt.bar(x = df2['时间'],height = df2['NO'],label = 'NO'
        ,bottom = df2['SO2'],tick_label = ['1日','2日','3日','4日','5日'])#将第二个画在第一个上面
plt.bar(x = df2['时间'],height = df2['NO2'],label = 'NO2',
        bottom=df2['SO2']+df2['NO'],tick_label = ['1日','2日','3日','4日','5日'])#将第三个画在第二个和第三个上面
plt.legend(bbox_to_anchor = (1.01,0.75))   # 设置图例坐标的位置（可以超过图形）
plt.close()


#在蔡志明的博客里有更有效的方法进行绘制
df2.plot(kind = 'bar',stacked =True)#可以通过stacked参数来判断，是否需要进行
