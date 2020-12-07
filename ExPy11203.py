# 파이썬 기초부터 활용까지 (2020.09)
# [12과] 엑셀 작업

t = '''김인문, 010-2244-3545, 상계동 237번지, abc@naver.com,p
박동식, 010-4456-9988, 삼성동 699번지, kbs@daum.net,p
최전문, 010-6600-0998, 역삼동 855번지, 222@daum.net,p
박동훈, 010-5500-0922, 방학동 667번지, aaa@naver.com,f
이형호, 010-5621-2356, 구로동 577번지, kim@gmail.com,p
한희훈, 010-5978-3434, 시흥동 522번지, donghyun@naver.com,f
지동석, 010-2202-4508, 영등포 434번지, bbb@gmail.com,f
황인숙, 010-2222-0909, 도봉동 333번지, sss@daum.net,p
최철훈, 010-5649-0908, 보문동 342번지, toto@daum.net,p'''

from openpyxl import *

t = t.split('\n')

# print(type(t), len(t), t)

for i in range(len(t)):
    t[i] = t[i].split(',')

# print(type(t), len(t), t)
#
# for i in range(len(t)):
#     for j in range(len(t[i])):
#         print(i, j, t[i][j])

wb = Workbook()

sh = wb.active
for i in range(len(t)):
    for j in range(len(t[i])):
        sh.cell(i+1, j+1).value = t[i][j]

wb.save('ExPy11203.xlsx')
