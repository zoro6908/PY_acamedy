# 파이썬을 활용한 데이터 분석 및 시각화 [3과] Pandas
# DataFrame 합치는 방법
import pandas as pd

sal2016 = pd.DataFrame({ '이름' : ['홍길동', '일지매', '전우치'],
                        '금여' : [200, 150,250]})
sal2017 = pd.DataFrame({ '이름' : ['일지매', '강감찬', '전우치', '홍길동'],
                         '급여' : [180, 210, 270, 220]})

# concat 함수이용
sal_concat1 = pd.concat([sal2016, sal2017])
print(sal_concat1)

# concat 함수이용 :
sal_concat2 = pd.concat([sal2016, sal2017], axis=1)
print(sal_concat2)

# concat 함수이용 : join(공통적으로 존재한 데이터만 표기)
sal_concat3 = pd.concat([sal2016, sal2017], axis=1, join='inner')
print(sal_concat3)

# merge 함수이용 : 왼쪽리스트 기준
sal_merge1 = pd.merge(sal2016, sal2017, on='이름')
print(sal_merge1)

# merge 함수이용 : 오른쪽 리스트 기준
sal_merge2 = pd.merge(sal2016, sal2017, on='이름', how='right')
print(sal_merge2)
