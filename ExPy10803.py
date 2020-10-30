# 파이썬 기초부터 활용까지 (2020.09)
# [8과] 함수(function) 1

# 본체와 함수간 데이터 흐름
# 전역에서 지역변수를 사용할 수 있나 -> X
# 함수지역에서 전역변수를 사용할 수 있나 -> O : 하지만 할당하는 순간 지역화
# 특정함수에서 다른 함수 변수를 사용할 수 있나 -> X
# 전역변수와 동일한 이름의 변수를 지역에서 사용할 수 있나 -> O : 하지만 별개
# 전역에서 넘어온 값을 지역에서 변경 가능한가 -> X

# 지역에서 전역변수를 정의할 수 있나 -> O global
def func():
    print(a, b)      # 지역에서 전역변수를 사용하고 있음, 무난히 사용

a = 10; b = 100
print(func())

# def func():
#     print(a, b)        # 지역에서 전역변수를 사용
#     a = 20             # UnboundLocalError: local variable 'a' referenced before assignment
#
# a = 10; b = 100
# print(func())

def func1():
     x = 100             # 지역에서 전역변수와 동일한 이름을 사용 : 전역변수 x 와 별개
     print(x)

x = 10
print(func1())


def func2(a):
    a = 10
    print('지역 :', a)        # 넘어오는 값을 바꿈 : 10

x = 100
print(func2(x))
print('전역 : ', x)           # 전역에서는 그대로 : 100

def func3():
    a[0] = 100               # 전역의 리스트 요소에 접근했다

if __name__ == '__main__':   # 프로그램의 시작점일 때만 아래 코드 실행, 외부 모듈일때는 수행하지 않음
    a = [1, 2, 3, 4]
    func3()
    print(a[0])               # 값이 변함 : 100

def func4(k):
    k[0] = 100                # 전역에서 넘어온 리스트 요소에 접근했다

if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행, 외부 모듈일때는 수행하지 않음
    a = [1, 2, 3, 4]
    func4(a)
    print(a[0])               # 값이 변함 : 100

def func5(k):
    k = [1, 2, 3, 4]

a = [100, 200, 300]
func5(a)
print(a)                      # 이번에는 불변 왜??? [100, 200, 300]