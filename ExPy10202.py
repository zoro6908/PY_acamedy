# 파이썬 기초부터 활용까지 (2020.09)
# [2과] 파이썬 기초 문법
# 2. 갌 대입하기
a = 255 + 488
print(a, type(a))

a = "안녕 파이썬"
print(a, type(a))

# 연산 대상 값의 type 구분
#
# a = "대한민국" + 345        # 문자와 숫자를 더할 수 없다 : TypeError: can only concatenate str (not "int") to str
# print(a)

a = "대한민국" + "345"
print(a)

# 형 번환 연산 str() int()
a = "대한민국"
a = "대한민국" + str(3700)
print(a)

a = input("숫자를 입력하세요..")
b = input("더할 숫자를 입력하세요...")

print(a + b)
print(int(a) + int(b))

# 기타 특징
# 여러 변수에 각각 대입
a, b, c, = 500, 600, 700
print(a, b, c)
# 여러 변수에 하나의 값 대입
a = b = c = 7000
print(a, b, c)
# 두 변수 값을 교환
a = 200
b = "파이썬"
print(a, b)
a, b = b, a
print(a, b)

# packing and unpacking
a = (1, 7, 3, 9, 5)           # 순서화 집단자료형인 튜플을 만든다
print(a)
print(a[2])                   # 집단자료형에서 개별데이터를 출력한다
# packing
k = 1, 2, 3
print("packing", k)           # packing
# unpacking
x, y, z = k
print("unpacking", x, y, z)   # unpacking

a = 20; b = 70; c = 50; print(a, b, c) # 세미콜론으로 구분 시 한 줄에 여러 문장 작성 가능

#  a = 100                             # 명령은 반드시 첫 번째 열부터 입력해야 한다 : IndentationError: unexpected indent

# 역슬래쉬 문자는 한 줄로 결합해 준다 문장이 긴 경우 유용
s1 = "korea"
s2 = " is beautiful"
s3 = " country"
# s4 = s1 + s2 + s3 와 동일한 문장이 된다
s4 = s1 + s2 + \
     s3
print(s4)

# 주석 : 코드설명이나 참고사항 등 필요시 샾문자(#) 활용