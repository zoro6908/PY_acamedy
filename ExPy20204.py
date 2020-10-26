# 파이썬을 활용한 데이터 분석 및 시각화 [2과]
# 연습문제 DataFrame
import pandas as pd
import sqlite3

df = pd.DataFrame({'이름' : ['허니버터칩', '감자깡', '새우깡'],
                   '수량' : [1, 2, 1],
                   '판매금액' : [800, 2400, 1200]})
print(df)

df.drop([0])
print(df.drop([0]))

print(df)