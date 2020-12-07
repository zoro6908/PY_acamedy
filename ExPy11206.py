# 파이썬 기초부터 활용까지 (2020.09)
# [12과] 엑셀 작업

# 파일 읽기

# import openpyxl
from openpyxl import *

wb = load_workbook('ExPy11203.xlsx')
sh = wb.active


for rw, data in enumerate(sh.rows):
    print(rw, data[0].value, data[1].value)     # 이름과 전화번호만 출력

for i in range(1, sh.max_row+1):
    point = 'A'+str(i)
    print(sh[point].value)                      # A1, A2, A3 이름 칼럼(B 로하면 2번째 칼럼)

for line in sh.columns:
    for col in line:
        print(col.value)
    print('--------------')

# 특정 셀집합에 대한 설택적 작업(슬라이싱)
m_cell = sh['C1':'E7']
for onerow in m_cell:
    for onecell in onerow:
        print(onecell.value)

# column과 row의 선택적 작업
colA = sh['A']
row5 = sh[5]

for ele in colA:
    print(ele.value)

for ele in row5:
    print(ele.value)