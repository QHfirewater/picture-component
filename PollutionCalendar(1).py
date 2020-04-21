# -*- encoding: utf-8 -*-
'''
@Author: sandwich
@Date: 2020-03-30 21:44:29
@LastEditTime: 2020-03-30 21:44:29
@LastEditors: sandwich
@Description: 绘制污染日历图
@FilePath: /plot/ZKPlot/PollutionCalendar.py
'''

# 导入用到的包
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
plt.rcParams["font.family"] = 'Arial Unicode MS'

def get_label(s):
    if s == '—':
        return '\n'*2
    else:
        reg = re.compile(r'.*?\((.*?)\).*?')
        res = '\n' + '\n'.join(reg.findall(s))
        return res + '\n'*(2-res.count('\n'))

def _map(series, func):
    return series.apply(func)


if __name__ == "__main__":
    #-------------------------将数据读取处理--------------------------#
    file = r'city_normal.xls'

    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']


    data = pd.read_excel(file, index_col=0)
    l = len(data.columns)
    citys = ['南平', '厦门', '宁德', '泉州', '漳州', '福州', '莆田', '龙岩']
    col = data.iloc[:, 1].dt.day.apply(lambda s: f'{s}日')
    dt = pd.DataFrame(data.iloc[:, 2:l:5].values.T, index=citys, columns=col)
    #-------------------------处理需要的自定义标签--------------------------#
    labels = pd.DataFrame(data.iloc[:, 3:l:5].values.T, columns=dt.columns, index=dt.index)
    labels = labels.apply(_map, args=(get_label,))
    labels = dt.astype(str) + labels
    #-------------------------开始绘图--------------------------#
    fig = plt.figure(figsize=(20, 8), dpi=120)
    colors = ['#00E400', '#FEFF00', '#FE7E00', '#FC0201','#871F78','#660000']
    bounds = [0, 50, 100, 150, 200,300,500]

    # 好在数据是均匀分布
    cm = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cm.N)
    # ax = sns.heatmap(dt, annot=labels, fmt='', vmin=0, vmax=500, cmap=cm, norm=norm,
    #                 linewidths=0.5, linecolor='gray', cbar_kws={'pad': 0.03},square= True)
    ax = sns.heatmap(dt, annot=labels, fmt='', vmin=0, vmax=500, cmap=cm, norm=norm,
                    linewidths=0.5, linecolor='gray', cbar=False)
    cb = ax.figure.colorbar(ax.collections[0]) #重新设置colorbar
    #-------------------------以防万一处理下--------------------------#
    plt.ylim(-0.5, len(dt))
    # plt.xlim(0, len(dt.columns)+0.5)
    #
    # plt.show()
    # plt.savefig('t.png')