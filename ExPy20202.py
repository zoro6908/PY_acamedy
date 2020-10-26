# 파이썬을 활용한 데이터 분석 및 시각화
# [2과] 판다스를 활용한 정형 데이터 처리 : 2) 판다스의  DataFrame 유형 활용
# 여러개의 컬럼이 있는 형태 : DataFrame

import pandas as pd

# Dictionary / List 활용
member1 = {'번호' : ['1번', '2번', '3번'],
          '이름' : ['홍길동', '전우치', '강감찬'],
          '생일' : [1975, 1980, 1992]}
member2 = pd.DataFrame(member1)
print(member2)

# DataFrame 조회 방법
print(member2['생일'])
# print(member2['생일', '이름'])

# 원하는 행 조회 방법 : 행번호 지정
print(member2.loc[0])
# 원하는 행 조회 방법 : 조건을 부여하여 조회하는 방법
print(member2.loc[ member2['번호'] >= '2번'])

member3 = {'번호' : ['1번', '2번', '3번', '4번', '5번'],
           '이름' : ['홍길동', '전우치', '강감찬', '홍길동', '일지매'],
           '매출' : [100, 200,250, 300, 150]}
member4 = pd.DataFrame(member3, columns= ['번호', '이름', '매출'])
print(member4)
print(member4.loc[(member4['매출'] >=100) & (member4['매출'] <=200)])

# 열을 추가하는 방법
member5 = pd.DataFrame(member3, columns=['번호', '이름', '매출', '지역'])
print(member5)
member5['지역'] = ['서울', '부산', '대전', '대구', '광주']
print(member5)

# 행을 추가하는 방법
member5.loc[5] = ['6번', '호날두', 1985, '유벤투스']
print(member5)

# 행을 삭제하는 방법
member5.drop([0])
print(member5)

member5.drop(member5[member5.매출 > 200].index)
print(member5.drop(member5[member5.매출 > 200].index))
print(member5)
