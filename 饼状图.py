#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/15/2020 2:19 PM
# @Author : QH
# @Site : WUXI
# @File : 饼状图.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = [12,15,11,8,12]
y = ['lili','lucy','john','mary','frank']
colors = ['yellow','red','green','blue','purple']
explode = [0,0,0.1,0,0]
plt.pie(x,explode = explode,colors = colors,labels = y,autopct = ' %.1f%%',pctdistance = 0.5,labeldistance = 1.1,startangle =120,radius = 1,counterclock = False,
        wedgeprops = {'linewidth':1.5,'edgecolor':'green'},textprops = {'fontsize':10,'color':'red'})
plt.title('每个人的销售额',pad=10)