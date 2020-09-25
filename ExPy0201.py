# 1. 변수

kor = 67
eng = 88
mat = 79
tot = kor + eng + mat
print(tot)

print(kor, eng, mat, tot)

print("국어: ", kor, "영어 : ", eng, "수학 : ", mat, "총점 : ", tot)

# 1.1 변수 이름 규칙
_kor = 34
print(_kor)

# 숫자로 시작할 수 없다
# 2eng = 125
# SyntaxError: invalid syntax
#
# 특수문자(%) 때문에 에러
# eng % 5 = "우리나라"
# SyntaxError: cannot assign to operator
#
# 한글 변수명은 가능
사람 = 79
print(사람)
#
# for는 예약어
# for = 25
# SyntaxError: invalid syntax
#
# 예약어 리스트
import keyword
print(keyword.kwlist)
