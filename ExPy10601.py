# 파이썬 기초부터 활용까지 (2020.09)
# [6과] list(리스트)

my_list = ['한국', '미국', '중국', '일본']

print(my_list)
print(my_list[0])    # 첫번째 요소 접근
print(my_list[3])    # 네번째 요소 접근
print(my_list[-1])   # 음수 인덱스 사용 (마지막)
# print(my_list[5])  # IndexError: list index out of range
print(len(my_list))  # len() 함수 사용 : 요소의 갯수
print(my_list[0:2])  # 슬라이싱 : 0번쩨 요소, 1번째 요소

if "미국" in my_list: # in 연산자
    print("미국 있음~~~")

my_list[3] = '인도네시아'  # 요소내용 변경
print(my_list)

my_list[2] = 2500         # 숫자 대입
print(my_list)