# 파이썬 기초부터 활용까지 (2020.09)
# [4과] 제어문1
# while문
# break : 반봅수행 블록을 즈시 벗어난다.
# continue : 조건 시작점으로 jump

# 1~100까지 짝수를 더하는 프로그램
# 방법1
i = 0
result1 = 0

while i < 100:
    i = i + 1
    if i % 2 == 0:
        result1 = result1 + i

print('방법1 : {0}'.format(result1))

# 방법2 : break
j = 0
result2 = 0

while True:
    if j == 100:
        break
    j = j + 1
    if j % 2 == 0:
        result2 =  result2 + j

print('방법2(break) : {0}'.format(result2))

# 방법3 : continue
k = 0
result3 = 0

while k < 100:
    k = k + 1
    if k % 2 != 0:
        continue

    result3 = result3 + k

print('방법3(continue) : {0}'.format(result3))