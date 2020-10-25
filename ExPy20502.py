# 막대 그래프 활용하기
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('C:\Temp\전염병발병현황_년도별_2.csv', encoding = 'euc-kr', index_col='년도')
df.head(10)

fig = plt.figure(figsize = (20, 10))
ax = plt.add_subplot(111)

wt = np.array(range(len(df)))
w = 0,1

for i in df.colums :
    ax.bar(wt, df[i], width = w, label = i)
    wt = wt + w

ax.set_xticks(np.array(range(len(df))))
ax.set_xticklabels(df.index, fontproperties = font)
ax.set_xticklabels('발생건수', fontproperties = font)
ax.legend()
plt.show()