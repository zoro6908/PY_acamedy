# 파이썬 기초부터 활용까지 (2020.09)
# [9과] 함수(function) 2

# 응용문제 : 제곱, 세제곱, 네제곱 정의하고 함수와 리스트를 넘기면 결과를 되돌려 주는 함수를 만드시요
def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

def agency(func, arg_list):
    result = list()
    for i in arg_list:
        result.append(func(i))
    return result

base = [1, 2, 3, 4, 5]
a = agency(square, base)
print(a)                                         # [1, 4, 9, 16, 25]
print(agency(cube, base))                        # [1, 8, 27, 64, 125]
print(agency(quad, base))                        # [1, 16, 81, 256, 625]
print(agency(quad, [3, 6, 7, 8, 11, 20]))        # [81, 1296, 2401, 4096, 14641, 160000]
