# 파이썬 기초부터 활용까지 (2020.09)
# [5과] 제어문2

# for문(연습문제) : 숫자 두개를 입력 받아서 두 개의 숫자 사이에 존재하는 모든 자연수의 합을 출력하는 프로그램

# 방법 1
a = input('시작 숫자를 입력하세요?.....')
b = input('끝 숫자를 입력하세요?.....')

a = int(a); b = int(b); sum = 0

for i in range(a, b + 1):
    sum = a + i

print(sum)

# 조건 : 7의 배수는 제외, 합이 2000이 넙어가면 프로그램 종료


a = input('시작 숫자를 입력하세요?.....')
b = input('끝 숫자를 입력하세요?.....')

a = int(a); b = int(b); sum = 0

while True:
    for i in range(a, b + 1):
        if i % 7 == 0:
            print('{0:3d}....... 7의 배수'.format(i))
        else:
            sum = sum + i
            print('{0:3d}..........{1:5d}'.format(i, sum))

        if i >= b or sum > 2000:
            break
    break
print('\n프로그램을 종료합니다.')

# 방법 2
while True:
    a = input('시작 숫자를 입력하세요?.....')
    b = input('끝 숫자를 입력하세요?.....')

    if not a.isnumeric() or not b.isnumeric():
        print('\n프로그램을 종료합니다.')
        break

    a = int(a); b = int(b); sum = 0

    for i in range(a, b+1):
        if i % 7 == 0:
            print('{0:3d}....... 7의 배수'.format(i))
            continue

        sum = sum + i
        print('{0:3d}..........{1:5d}'.format(i, sum))

        if i >= b or i >=2000:
            break