# 파이썬 기초부터 활용까지 (2020.09)
# [2과] 파이썬 기초 문법
# [변수]

kor = 67
eng = 88
mat = 79
tot = kor + eng + mat
print(tot)

print(kor, eng, mat, tot)

print("국어: ", kor, "영어 : ", eng, "수학 : ", mat, "총점 : ", tot)

# 변수 이름 규칙
_kor = 34
print(_kor)


# 2eng = 125             # 숫자로 시작할 수 없다 : SyntaxError: invalid syntax
# eng % 5 = "우리나라"   # 특수문자(%) 때문에 에러 : SyntaxError: cannot assign to operator
사람 = 79                # 한글 변수명은 가능
print(사람)
# for = 25               # for는 예약어 : SyntaxError: invalid syntax

# 예약어 리스트 출력
import keyword
print(keyword.kwlist)

# 내장 함수등을 변수로 사용하지 말자
# print = 2350                 # 내장함수를 변수로 사용
# print("대한민국")             # 함수의 기능을 잃었다
# input = '우리나라'              # 내장함수를 변수로 사용
# a = input(' 나이를 입력하시요')  # 함수의 기능을 잃었다

# 대소뮨자 구분에 유의
a, A = 255, 600
print(a, A)
