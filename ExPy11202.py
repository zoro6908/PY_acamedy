# 파이썬 기초부터 활용까지 (2020.09)
# [12과] 엑셀 작업

from openpyxl import *
t = '홍길동, 010-0000-xxxx, 성남시 가동111번지, 성남전자, abc@abc.co.kr, p'
t = t.split(',')
print(type(t), t)

wb = Workbook()
ws = wb.active

for i, ele in enumerate(t):
    ws.cell(1, i+1, ele)
wb.save('ExPy11202.xlsx')