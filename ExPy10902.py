# 파이썬 기초부터 활용까지 (2020.09)
# [9과] 함수(function) 2

# 재귀호출함수 : 자기 자신을 호출하는 함수 (주의:무한루프, 응용:팩토리얼, 피보나치 등)

# factorial구하기 5! ---> 5 * 4 * 3 * 2 * 1 = x * factorial(x -1)
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x -1)
#
# while True:
#     n = input('\n팩토리얼을 구할 숫자는???')
#     if n.isnumeric():
#         res = factorial(int(n))
#         print(res)
#         print('프로그램을 종료하려면 문자를 입력하세요.')
#     else:
#         print('프로그램을 종료합니다.')
#         break
#
# fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21.... ---> 처음 두항음 1, 세항부터는 앞 두합의 합
def fibonaccci(n):
    if n <= 2:
        return 1
    else:
        return fibonaccci(n - 2) + fibonaccci(n - 1)

f = []
while True:
    k = input('\n피노나치 몇 단계까지 구성할까요???')
    if k.isnumeric():
        f.clear()
        k = int(k)
        for i in range(1, k + 1):
            f.append(fibonaccci(i))
        for i in f:
            print(i, end=' ')
    else:
        print('종료합니다.')
        break
