# 파이썬 기초부터 활용까지 (2020.09)
# [9과] 함수(function) 2

# 람다식(익명함수) : 이름 없이 인수와 수식을 통해 값을 반환하는 한 줓 함수(중요)
k = lambda x, y : x * y
print(k(10, 5))                         # 50

p = lambda x, y : (x+y, x-y, x*y)
print(p(6,4))                           # (10, 2, 24)

mul = lambda x, y, z : x*y*z
print(mul(5,7,9))                       # 315

m = ["파이썬", lambda x : x*x, 100]
print(m[0])                             # 파이썬
print(m[1])                             # <function <lambda> at 0x038C3268>
print(m[2])                             # 100
print(m[1](5))                          # 25

print((lambda x,y,z : x*y*z)(5,7,9))    # 315
