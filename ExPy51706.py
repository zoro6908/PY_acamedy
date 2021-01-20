# 파이썬 도장 깨기
# Unit 17. While 반복문을 Hellow World 100번 출력하기

# 심사문제 : 교통 카드 잔액 출력 하기 1회 요금은 1,350입니다.

a = int(input('현재 금액을 입력하세요 : '))
b = 1350
i = 0

while a >= b:
    a = a - b
    i = i + 1
    print(i, '회, ', '잔액 : ', a)
