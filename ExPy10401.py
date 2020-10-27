# 파이썬 기초부터 활용까지 (2020.09)
# [4과] 제어문1
# [제어문] : if, while, for, try
# if문
# score = input('점수를 입력하세요')
# score = int(score)
#
# if score >= 60:
#     print('합격하였습니다.')
#     print('축하합니다.')
# else:
#     print('다읍기회에~~')

# 비교 연산자 : 좌우의 값을 비교하여 논리상수인 True 혹은 False 반환
# a > b, a < b, a >= b, a <= b, a == b, a != b
print(60 > 40)           # True
print(60 == 70)          # False
a = 20; print(a > 10)    # True
print(a - 10 == 10)      # True
print('kbs' > 'sbs')     # False : 사전순 비교
# print(a > '10')        # TypeError: '>' not supported between instances of 'int' and 'str'
print(a != '10')         # True
# 논리상수인 True와 False는 각각 1과 0 값이 할당되어 있음
if 10: print('ppppp')          # ppppp
if 'abc': print('ppppp')       # ppppp
print(True - 1)                # 0

if True - 1:                   # sssss : 거짓으로 인식
    print('ppppp')
else:
    print('sssss')

if ' ': print('ppppp')         # ppppp : 0이 아닌 숫자값과 문자값이 존재하나느 갓은 True
else: print('sssss')

if '': print('ppppp')          # sssss : 거짓으로 인식
else: print('sssss')           # 0, 할당되지 않은 빈데이터 등은 False로 취급

# 논리연산자 : not a, a and b, a or b : 좌우의 논리값을 비교하여 True와 False를 반환
if 5 > 2 and 'a' < 'b': print('all True')   # all True
a, b, c, d = 40, 20, 60, 70

if a > b and c < d: print('ttttt')          # ttttt

if a > b and b > d: print('ttttt')          # fffff
else: print('fffff')

if not a - 40: print('ttttt')               # ttttt
else: print('fffff')

if a < 0 or d > 20: print('ttttt')          # ttttt
else: print('fffff')
