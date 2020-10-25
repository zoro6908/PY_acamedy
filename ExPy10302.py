# 파이썬 기초부터 활용까지 (2020.09)
# [3과] 연산문

# 2. 문자연산
# 큰 따움표, 작은 따옴표 둘 다 사용 가능
a = "파이썬 좋아"; b = 'korea'
print(a); print(b)
a = "파이썬 프로그래밍 \
문자열 표현방식"
print(a)
# 따옴표 자체를 문자로 다룰 때는?
# p1 = 'I'm a boy'; print(p1)      # SyntaxError: invalid syntax
p1 = "I'm a boy"; print(p1)        # 작은 따옴표 표현을 위해 큰 따옴표로 묶어준다
p2 = "You don't know"; print(p2)
p3 = 'I\'m a boy'; print(p3)       # 파이썬 제어문자 \를 이용한다
p4 = "korea\tchina"; print(p4)     # 줄바꾸기 : \n, 탭 : \t, ESC : \e, 백스페이스 : \b, , 문자자체 : \에 붙여씀 예 : \"
# 문자열 결합 연산
c = a + b; print(c)                # 덧셈기호를 이용한 문자열 결합
d = 'America' * 3; print(d)        # 곱셈기호를 이용한 문자 반복
# 인덱스를 사용한 접근(indexing)
# 문자열은 일종의 순서형데이터로서 튜플형과 유사
a = '우리나라 대한민국'             # 양의 인덱스 : 0, 1, ... 8, 음의 인덱스 : -9, -8, ... -1
print(a[0]); print(a[1]); print(a[-9])
# print(a[9])                      # 인덱스가 벗어나서 에러 발생 : IndexError: string index out of range
# 슬라이싱(slicing) : [시작:끝(직전):간격]
print(a[1:6]); print(a[0:7]); print(a[-9:-6]); print(a[-3:-9]); print(a[-3:-9:-1])
print(a[:])             # 슬라이싱 시작과 끝 생략
print(a[:6])            # 시작지점 생략
print(a[::3])           # 3인덱스씩 건너 뛰며 취한다 : 0, 3, 6 인덱스 출력
# 부분 문자열은 수정할 수 없다~~
a = '우리나라 대한민국'
# a[0] = '사'           # 내용 수정 불가 : TypeError: 'str' object does not support item assignment
a = '아름다운 우리강산'  # 새롭게는 가능
print(a)
a = '예쁜 ' + a[5:]     # 과거의 내용을 이용해 새로 구성 가능
print(a)

# for를 이용한 전체 순환
my_string = '아름다운 우리강산'
for ch in my_string:    # 한자 한자씩 세로로
    print(ch)

for ch in my_string:    # 가로로
    print(ch, end='')

print(20,30,40, sep='::')

abp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(len(abp))         # 문자열 길이 알아내기 : len() 함수
print('abc' in abp); print('ABC' in abp)        # 부분 문자열 검사 : in 연산자
print(abp.find('jkl'))  # 부분문자열 위치 찾기 : find() 메소드 : .find(문자열, 시작점, 끝점)
print(abp.find('JKL'))  # 못찾으면 -1 반환(-1은 False를 의미), 찾으면 찾은 위치 반환
print('우리나라 우리 우리나라 우리'.count('우리'))  # 문자열 갯수 체크 : count() 메서드
print('방네' in '동네방네') #문자열 점검 있으면 True 반환
print(abp.lower())      # 소문자전환 메서드 : lower()
print(abp.upper())      # 대문자전환 메서드 : upper()
print('abCD'.swapcase()) # 대소문자 쌍방전환

data1 = '이낙연, 박종필, 윤호중, 황대영'
print(data1.split(','))  # 문자의 분리 : split 메서드(리스트 구조가 얻어짐)
data2 = data1.split(',')
for ch in data2:
    print(ch)

data3 = ':'.join(data2); print(data3)  # 문자의 결합 : join() 메서드
a = '우리나라 우리나라'; print(a.replace('우리', '남의')) # 문자열 대체 : replace() 메서드
a = '우리나라 '; print(a.strip(' '))    # 공백없애기 : strip(), rstrip(), lstrip() 메서드
a = '*****우리나라*****'; print(a.strip('*'))
a = '*****우리나라*****'; print(a.lstrip('*'))
a = '*****우리나라*****'; print(a.rstrip('*'))
a = 'abc'; print(a.isalpha())    # 문자열 내용 검사 메소드 : .isalpha() :문자열이 영문자나 유니코드인가)
a = '123.5'; print(a.isalnum())  # 문자열 내용 검사 메소드 : .isalnum() : 문자열이 숫자, 영문자, 유니코드인가)
a = '123.5'; print(a.isnumeric())  # 문자열 내용 검사 메소드 : .isnummeric() : 문자열이 숫자인가)
a = 'abc'; print(a.islower())  # 문자열 내용 검사 메소드 : .islower() : 소문자로만 되어있나)
a = 'Abc'; print(a.isupper())  # 문자열 내용 검사 메소드 : .isupper() : 대문자로만 되어있나)
a = ' '; print(a.isspace())        # 문자열 내용 검사 메소드 : .issapce() : 공백으로만 되어 있나)

# 문자열 서식 지정 메서드
print('{0} {1:>7.2f}'.format(250, 43.9875)) # >:우측정렬, 7.2:최소 7자리확보, 소수점이하 두자리, f:floating point 자료형
print('{}.....{}'.format(49, 290))
print('{1}.....{0}'.format(49, 290))
print('{0:>3d}.....{1:10d}'.format(49, 290))
print('십진{0:d} 이진{0:b} 8진{0:o} 16진{0:x}'.format(255))