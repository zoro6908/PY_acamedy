# ExPy9xxxx 파이썬 개인 연습
# pandas
# https://dandyrilla.github.io/2017-08-12/pandas-10min/
# https://pandas.pydata.org/docs/user_guide/index.html

import pandas as pd
import numpy as np

# 1. 데이터 오브젝트 생성하기
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# # print(type(s), s)
# print(s)
# # 0    1.0
# # 1    3.0
# # 2    5.0
# # 3    NaN
# # 4    6.0
# # 5    8.0
# # dtype: float64
#
#
# dates = pd.date_range('20130101', periods=6)
# print(dates)
# # DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
# #                '2013-01-05', '2013-01-06'],
# #               dtype='datetime64[ns]', freq='D')
#
# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
# print(df)
# #                    A         B         C         D
# # 2013-01-01 -2.442341  0.665228  0.233229  0.162321
# # 2013-01-02  0.080594  1.618536  0.126620 -1.186379
# # 2013-01-03  2.149113 -0.441872  0.604208 -0.024448
# # 2013-01-04  0.991242 -1.030692 -1.001032 -0.460890
# # 2013-01-05 -0.332589  0.067753 -0.042324 -1.174614
# # 2013-01-06  0.154003 -0.374657 -0.697021 -0.245108

# 여러 종류의 자료들이 담긴 딕셔너리(dict)를 넣어주어 만드는 법
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
# print(df2)
# #      A          B    C  D      E    F
# # 0  1.0 2013-01-02  1.0  3   test  foo
# # 1  1.0 2013-01-02  1.0  3  train  foo
# # 2  1.0 2013-01-02  1.0  3   test  foo
# # 3  1.0 2013-01-02  1.0  3  train  foo
#
# # DataFrame 의 컬럼들은 각기 특별한 자료형을 갖고 있을 수 있다
# print(df2.dtypes)
# # A           float64
# # B    datetime64[ns]
# # C           float32
# # D             int32
# # E          category
# # F            object
# # dtype: object

# print(dir(df2))
# In [13]: df2.<TAB>
# df2.A                  df2.bool
# df2.abs                df2.boxplot
# df2.add                df2.C
# df2.add_prefix         df2.clip
# df2.add_suffix         df2.clip_lower
# df2.align              df2.clip_upper
# df2.all                df2.columns
# df2.any                df2.combine
# df2.append             df2.combine_first
# df2.apply              df2.compound
# df2.applymap           df2.consolidate
# df2.as_blocks          df2.convert_objects
# df2.asfreq             df2.copy
# df2.as_matrix          df2.corr
# df2.astype             df2.corrwith
# df2.at                 df2.count
# df2.at_time            df2.cov
# df2.axes               df2.cummax
# df2.B                  df2.cummin
# df2.between_time       df2.cumprod
# df2.bfill              df2.cumsum
# df2.blocks             df2.D


# print(pd.bdate_range('20200101', '20200201'))
# DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-06',
#                '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10',
#                '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16',
#                '2020-01-17', '2020-01-20', '2020-01-21', '2020-01-22',
#                '2020-01-23', '2020-01-24', '2020-01-27', '2020-01-28',
#                '2020-01-29', '2020-01-30', '2020-01-31'],
#               dtype='datetime64[ns]', freq='B')

# 2. 데이터 확인하기 (Viewing Data)

