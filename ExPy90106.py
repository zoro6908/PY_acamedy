# ExPy9xxxx 파이썬 개인 연습
# pandas
# https://dandyrilla.github.io/2017-08-12/pandas-10min/
# https://pandas.pydata.org/docs/user_guide/basics.html

# 5. 연산 (Operations)

import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)

# df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# data = {'A':[1, 2, 3, 4, 5, 6], 'B':[1, 2, 3, 4, 5, 6], 'C':[1, 2, 3, 4, 5, 6], 'D':[1, 2, 3, 4, 5, 6]}
# df = pd.DataFrame(data, index=dates)

data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [11, 12, 13, 10], [11, 12, 3, 4], [11, 12, 13, 10]]
df = pd.DataFrame(data, index=dates, columns=list('ABCD'))


print(df)
#                    A         B         C         D
# 2013-01-01  0.805071 -2.164387 -1.198795  0.235786
# 2013-01-02 -1.627601 -0.432660  0.574830 -0.895947
# 2013-01-03  1.189210  0.871206  0.190652 -0.389701
# 2013-01-04 -1.022214 -0.145620  0.238693 -0.090097
# 2013-01-05 -0.460052  0.277914  0.665454  0.409565
# 2013-01-06  0.753050 -0.005841  0.262368 -0.151970

# 통계적 지표들 (Stats)
# 평균 구하기. 일반적으로 결측치는 제외하고 연산

# print(df.mean())
# # A   -0.060423
# # B   -0.266565
# # C    0.122200
# # D   -0.147061
# # dtype: float64
#
# # mean() 함수의 인자로 1을 주게 되면 컬럼이 아닌 인덱스를 기준으로 연산
# print(df.mean(1))
# # 2013-01-01    0.062659
# # 2013-01-02    0.954058
# # 2013-01-03   -0.032940
# # 2013-01-04    0.443181
# # 2013-01-05   -1.557883
# # 2013-01-06    0.194778
# # Freq: D, dtype: float64

# s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
# print(s)
#
# # pandas 는 맞추어야 할 축만 지정해 준다면 자동으로 해당 축을 기준으로 맞추어 연산을 수행
# # 존 데이터 프레임의 인덱스가 2013-01-03, 04, 05 인 모든 컬럼에 해당하는 값에 각각 1.0, 3.0, 5.0 를 빼준 값이 결과로 나옵니다.
# # 또한 결측치가 존재하는 경우에는 계산이 불가능 하므로 NaN 으로 표시된다는 것도 알 수 있습니다.
# print(df.sub(s, axis='index'))
# #                    A         B         C         D
# # 2013-01-01       NaN       NaN       NaN       NaN
# # 2013-01-02       NaN       NaN       NaN       NaN
# # 2013-01-03 -1.009641 -2.062061 -2.008451 -0.503947
# # 2013-01-04 -2.764959 -4.490075 -1.236707 -2.994800
# # 2013-01-05 -5.937384 -7.923094 -5.222245 -4.198384
# # 2013-01-06       NaN       NaN       NaN       NaN

# # 함수 적용하기 (Apply)
# print(df.apply(lambda x: x.max() - x.min()))
# # A    10
# # B    10
# # C    10
# # D     8
# # dtype: int64
#
# print(df.apply(np.cumsum))
# #              A   B   C   D
# # 2013-01-01   1   2   3   4
# # 2013-01-02   6   8  10  12
# # 2013-01-03  15  18  21  24
# # 2013-01-04  26  30  34  34
# # 2013-01-05  37  42  37  38
# # 2013-01-06  48  54  50  48

# 문자열 관련 메소드들 (String methods)
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())