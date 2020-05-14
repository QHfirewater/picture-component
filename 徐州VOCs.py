#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 5/11/2020 5:17 PM
# @Author : QH
# @Site : WUXI
# @File : 徐州VOCs.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import os

#进行系统设置
print('开始进行数据的处理')
path_file = os.path.abspath('main.py')
path_file2 = os.path.dirname(path_file)
os.chdir(path_file2)
if not os.path.exists((str(path_file2) + str('\\处理后结果'))):
    os.makedirs((str(path_file2) + str('\\处理后结果')))

#读取相关数据
try:
    voc = pd.read_excel(r'徐州上传国家平台VOC数据（模板）.xlsx',sheet_name=0)
    mod = pd.read_excel(r'徐州上传国家平台VOC数据（模板）.xlsx',sheet_name=1)
except:
    print('导入数据错误')

#处理时间格式
try:
    voc['日期'] = voc['日期'] + ':00:00'
    date = voc['日期'].apply(lambda s :str(s).split()[0])
    date = date.apply(lambda x: '{}/{}/{}'.format(*x.split('-')))
    time = voc['日期'].apply(lambda s :str(s).split()[-1])
    voc['日期'] = date + ' ' + time
except:
    print('数据时间格式错误')

#数据处理
try:
    voc.fillna(-999.000,inplace = True)
    mod2 = mod.set_index(mod.columns[0],inplace=False)
    voc2 = voc.set_index(voc.columns[0],inplace = False)
    zong = pd.concat([mod2,voc2],join = 'inner',sort = False)
    zong.drop(index = ['时间','Time'],inplace =True)
    zong2  = pd.concat([mod2,zong],join = 'outer',sort = False)
    zong2.fillna('/',inplace = True)
    zong2.index.name = mod.columns[0]
except:
    print('数据合并错误')

print('开始导出数据')
zong2.to_excel(r'处理后结果\上传数据.xlsx')
input('请按<enter>键退出程序')
