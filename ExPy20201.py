# 파이썬을 활용한 데이터 분석 및 시각화
# [2과] 판다스를 활용한 정형 데이터 처리 : 1) 판다스의 Series 유형의 활용
# 컬럼이 판개 만 있는 형태 : Series, 인텍스 수정이 가능
# 컬리이 두개 이상인 형태 : DataFrame

import pandas as pd

member = pd.Series(['홍길동', '전우치', '강감찬', '스티브잡스'])
print(member)

member = pd.Series(['홍길동', '강감찬', '전우치', '스티브잡스'], index=['1번', '2번', '3번', '4번'])
print(member)

# Series 조회
print(member[0])
print(member['1번'])
# print(member[ ['1번'], ['3번'] ])
print(member['4번'])

# Dictionary 유형으로 생성
sal1 = {'홍길동' : 100, '일지매' : 130, '전우치' : 120}
sal2 = pd.Series(sal1)
print(sal2)

sal3 = {'홍길동' : 10, '전우치' : 12, '강감찬' : 20}
sal4 = pd.Series(sal3)
print(sal4)

# Series 연산 방법
print(sal2 + sal4)
print(sal4 - sal2)