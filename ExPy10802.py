# 파이썬 기초부터 활용까지 (2020.09)
# [8과] 함수(function) 1

# 응용문제 : 두 숫자가 들어 오면 합, 차, 곱, 나눗셈 결과를 반환해주는 함수를 작성
def cal(x, y):
    ad = int(x) + int(y)
    sb = int(x) - int(y)
    mt = int(x) * int(y)
    if y != 0:
        dv = int(x) / int(y)
    else:
        dv = '불능'
    return (ad, sb, mt, dv)

a = input('\n첫번째 숫자를 입력하세요?...')
b = input('두번째 숫자를 입력하세요?...')

result = cal(a, b)
print(result)
