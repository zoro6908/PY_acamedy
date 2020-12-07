# 파이썬 기초부터 활용까지 (2020.09)
# [12과] 엑셀 작업

# 행과 열의 사이즈 지정
# 행의 높이 : sheet.row_dimensions[인덱스].hight = 높이
# 열의 너비 : sheet.column_dimensions[열키].width = 너비
# 3행의 높이를 8로 높이고 싶으면 : ws.row_dimensions[3].height = 8
# C열의 너비를 20으로 넓히고 싶으면 : ws.column_dimensions['C'].width = 20

# t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# t = tuple(t)
#
# print(type(t), len(t), t)

t = 'ABCDEFGHIJKLMNOPQR'
t = tuple(t)

s = (8, 8, 12, 12, 10, 10, 10, 12, 12, 12, 12, 12, 12, 10, 10, 10, 10, 10)

print(type(t), len(t), t)
print(type(s), len(s), s)

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

for i in range(len(t)):
    ws.cell(1, i+1).value = t[i]
    ws.column_dimensions[t[i]].width = s[i]

wb.save('ExPy11204.xlsx')