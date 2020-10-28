# 파이썬 기초부터 활용까지 (2020.09)
# [5과] 제어문2

# for 문 : 집단형 자료에 대해 순환하며 정해진 문자들을 반복 처리
for ele in 10, 9, 5, 6:
    print(ele)

data = ['korea', 'america', 'japan', 'china']
for ele in data:
    print(ele)

# range() 함수 : range(시작, 끝, 간격) : 반복 수치 발생, 시작부터 끝 직전까지 간격을 두고 발생
for ele in range(5):  # 0 1 2 3 4
    print(ele, end=' ')
print('\n')

for ele in range(3, 9, 2):  # 3_5_7_
    print(ele, end='_')
print('\n')

# k = range(10, 2, -1)             # 10 9 8 7 6 5 4 3
# for ele in k:
#     print(ele, end=' ')
# print('\n')

k = range(10, 2)                   # 간격이 없으므로 값이 안 나온다
for ele in range(10, 2):
    print(ele, end=' ')

k = range(10, 2, -1)               # 10 9 8 7 6 5 4 3
for j in k:
    print(j, end=' ')