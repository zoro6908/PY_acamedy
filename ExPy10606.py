# 파이썬 기초부터 활용까지 (2020.09)
# [6과] list(리스트)
# 집단형 데이터 순환 정리

# 집단형 데이터 그냥 사용
data = ['성동일', '이문세', '조용필', '김수철']

for dt in data:
    print(dt, end=' ')

print('\n')

# range(), len() 사용 : 데이터를 직접 수정할 수 있어서 장점이 있음
data = ['성동일', '이문세', '조용필', '김수철']

for i in range(len(data)):
    print(i, ' ', data[i], end=' ')
print('\n')

# enumerate() 활용 : 열거자 함수
data = ['성동일', '이문세', '조용필', '김수철']

for i, dt in enumerate(data):
    print(i, ' ', dt, end=' ')