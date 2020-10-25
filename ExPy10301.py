# 파이썬 기초부터 활용까지 (2020.09)
# [3과] 연산문

# 1. 수치연산
print(398**2)      #지수

a = 55.6; b = 7
c = a + b          # 실수와 정수의 덧셈
print(c, type(c))  # 결과는 실수
s = int(c)         # int() 함수 사용
print(s)
k = s - 900
print(k)
k2 = abs(k)        # 절대치 함수
print(k2)

p = (10, 20, 90, 70, 8)   # 튜플 자료형
print(p)
print(max(p))             # 최대치 함수
print(min(p))             # 최소치 함수
print(sum(p))             # 합계 함수