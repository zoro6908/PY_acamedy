# 파이썬 기초부터 활용까지 (2020.09)
# [5과] 제어문2

# for문(연습문제) : 1부터 100까지 존재하는 자연수의 홀수 합과 짝수 합을 각각 구하는 프로그램

i = 0; odd = 0; even = 0

for ele in range(100):
    i = i + 1
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print('홀수 합 : ', odd, '\n', '짝수 합 : ', even)
