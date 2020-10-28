# 파이썬 기초부터 활용까지 (2020.09)
# [5과] 제어문2

# for문 (반복문의 중첩 연습문제) : 알파벳 쉬프트 출력

# 방법1 : 슬라이싱 사용
abp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('\n방법1 : 슬라이싱 *********')
for i in range(len(abp)):
    s = abp[i:26] + abp[0:i]
    print('{0:2d}    {1:s}'.format(i, s))

# 방법2
abp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('\n방법2 : for 중첩 *********')
for i in range(len(abp)):
    s = ''
    for j in range(i, len(abp)):
        s = s + abp[j]
    for k in range(0, i):
        s = s + abp[k]
    print('{0:2d}    {1:s}'.format(i, s))

# 방법3
abp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abp = tuple(abp)

print('\n방법3 : 튜플화 *********')
print(abp)

for i in range(len(abp)):
    s = ''
    for j in range(i, len(abp)):
        s = s + abp[j]
    for k in range(0, i):
        s = s + abp[k]
    print('{0:2d}    {1:s}'.format(i, s))