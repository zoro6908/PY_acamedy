# ExPy9xxxx 파이썬 개인 연습
# pandas

import pandas as pd
import openpyxl

# 엑셀파일 생성
# df = pd.DataFrame([['우상호', 1000, 9, 15, 100], ['추매애', 2000, 8, 15, 200],
#                    ['홍준표', 3000, 10, 16, 200], ['김종인', 4000, 8, 16, 300],
#                    ['윤석열', 3500, 11, 18, 100]], columns=['이름', '시급', '출근시간', '퇴근시간', '생산량'])
#
# df.to_excel('ExPy90102.xlsx', index=False)

# 엑셀파일 읽기
df = pd.read_excel('ExPy90102.xlsx')
# print(df)
# print(df['이름'])

# 컬럼추가
df['근무시간'] = df['퇴근시간'] - df['출근시간']

# 컬럼추가
df['시간당생산량'] = df['생산량'] / df['근무시간']

# print(df)

# 정렬
df = df.sort_values(by=['시간당생산량'], ascending=False)
print(df)

