# 파이썬 기초부터 활용까지 (2020.09)
# [10과] 튜플과 딕션너리

# 튜플 : 변수 = (값)
my_tup = ('한국', '미국', '중국', '일본')
print(my_tup[2:3])                       # ('중국',)
print(my_tup[2])                         # 중국
print(my_tup[0:3])                       # ('한국', '미국', '중국')
print(my_tup[-4])                        # 한국
# my_tup[0] = '태국'                        # TypeError: 'tuple' object does not support item assignment
a =  1, 2, 3                             # 패킹 a = (1, 2, 3) 과 동일
print(a)                                 # (1, 2, 3)
x, y, z = a                              # 언패킹
print(x, y, z)                           # 1 2 3
print(type(x))                           # <class 'int'>
a = [100, 200, 300]
print(type(a), a)                        # <class 'list'> [100, 200, 300]
b = list(a)
print(type(b), b)                        # <class 'list'> [100, 200, 300]
c = tuple(a)
print(type(c), c)                        # <class 'tuple'> (100, 200, 300)
