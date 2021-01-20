# ExPy9xxxx 파이썬 개인 연습
# pandas
# https://dandyrilla.github.io/2017-08-12/pandas-10min/
# https://pandas.pydata.org/docs/user_guide/basics.html

# 7. 묶기 (Grouping)

import pandas as pd
import numpy as np

df = pd.DataFrame({'name':['kim', 'park', 'kim', 'park', 'choi', 'lee', 'kim', 'lee'],
                   # 'prod':['pepero', 'pepero', 'chocopie', 'chocopie', 'saeukang', 'saeukang', 'bean', 'bean'],
                   'product':['빼뺴로', '빼뺴로', '초코파이', '초코파이', '새우깡', '새우깡', '빈츠', '빈츠'],
                   'dept':['영업1팀', '영업1팀', '영업1팀', '영업1팀', '영업2팀', '영업2팀', '영업1팀', '영업2팀'],
                   'sales_qty':[100, 200, 300, 100, 200, 300, 100, 200],
                   'sales_amt':[10000, 2000, 3000, 1000, 1000, 2000, 3000, 4000]})
print(df)
#    name product  sales_qty  sqles_amt
# 0   kim     빼빼로        100      10000
# 1  park     빼빼로        200       2000
# 2   kim    초코파이        300       3000
# 3  park    초코파이        100       1000
# 4  choi     새우깡        200       1000
# 5   lee     새우깡        300       2000
# 6   kim      빈츠        100       3000
# 7   lee      빈츠        200       4000

print(df.groupby(['name']).sum())
#       sales_qty  sqles_amt
# name
# choi        200       1000
# kim         500      16000
# lee         500       6000
# park        300       3000

print(df.groupby(['name', 'product']).sum())
# name product
# choi 새우깡            200       1000
# kim  빈츠             100       3000
#      빼뺴로            100      10000
#      초코파이           300       3000
# lee  빈츠             200       4000
#      새우깡            300       2000
# park 빼뺴로            200       2000
#      초코파이           100       100

# 하나의 쉬트로 저장
# df.to_excel('ExPy90108.xlsx', index=False)
df1 = df.groupby(['name']).sum()
df2 = df.groupby(['name', 'product']).sum()
df3 = df.groupby(['dept', 'name', 'product']).sum()
df4 = df.pivot_table(df, index=['name', 'product'], columns=['dept'])

# 여러개의 쉬트로 저장
with pd.ExcelWriter('ExPy90108.xlsx', index=False) as writer:
    df.to_excel(writer, sheet_name='Data')
    df1.to_excel(writer, sheet_name='name sum')
    df2.to_excel(writer, sheet_name='name product sum')
    df3.to_excel(writer, sheet_name='dept name product sum')
    df4.to_excel(writer, sheet_name='pivot sum')
