# 파이썬 웹 스크랭핑 강의 2
# https://nadocoding.tistory.com/10

# 정규식 활용 re
# 정규식이란? 주민번호, 이메일 주소, 차량번호, IP 주소를 점검할 때 사용한다
# docs.python.org or w3school 참조

# 1. p = re.compile('원하는 형태')
# 2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall('비교할 문자열') : 일치하는게 모든 것을 "리스트" 형태로 반환
# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe(X)
# ^ (^de)   : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)   : 문자열의 끝 > case, base (O) | face (X)

import re

# 4자리 중 3가지 만 기억될 대 : ca?e, 그러면 cafe, cace, cade 여러 가지를 생각해 볼 수 있는데 정규식을 사용하면
p = re.compile('ca.e')   #  패턴을 만들어 준다

# m = p.match('case')
# # m = p.match('caffe')
# # print(m.group())      # 매치되면 문자열 출력, 아니면 에러 발생
# if m:
#     print(m.group())
# else:
#     print('매칭되지 않음')

# 위내용을 함수로 표현
def print_match(m):
    if m:
        print('m.group():', m.group())    # 일치하는 문자열 반환
        print('m.string:', m.string)  # 입력받은 문자열 반환
        print('m.start():', m.start())    # 일치하는 문자열의 시작 index 반환
        print('m.end():', m.end())        # 일치하는 문자열의 끝 index 반환
        print('m.span():', m.span())      # 일치하는 문자열의 시작과 끝 index 반환
    else:
        print('매칭되지 않음')

m = p.match('careless')      # care 출력 : match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

m = p.search('good care')    # care 출력 : search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst = p.findall('good care cafe')   # care cafe 출력 : findall : 일치하는게 모든 것을 리스트 형태로 반환
print(lst)
