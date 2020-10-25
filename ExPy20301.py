# 파이썬을 활용한 데이터 분석 및 시각화 [3과]
# 엑셀파일을 불러올 경우 xlrd 패키지 설치가 요구됨
# CSV파일 읽어오기
import pandas as pd

pop1 = pd.read_csv("C:\\Temp\\pop_2014.csv", encoding="euc-kr")
print(pop1.head(10))

pop2 = pd.read_excel("C:\\Temp\\경상남도_년도별_지역별_인구수_2014년.xlsx")
print(pop2.head(10))

# 행번호 지정하여 불러오기 : header (입력한 줄 번호부터 출력)
pop3 = pd.read_excel("C:\\Temp\\경상남도_년도별_지역별_인구수_2014년.xlsx", header=1)
print(pop3.head(10))

# 컬럼 지정하여 불러오기 : usecols + 엑셀시트의 컬럼명 (입력한 줄 번호부터 출력)
pop4 = pd.read_excel("C:\\Temp\\경상남도_년도별_지역별_인구수_2014년.xlsx", usecols="A, D, E")
print(pop4.head(10))

# 컬럼 이름 변경하기
pop4.rename(columns={pop4.columns[1] : '남자',
                     pop4.columns[2] : '여자'}, inplace=True)
print(pop4.head(5))

# 데이터 정렬 방법
pop5 = pop2.sort_values(by="행정구역명", ascending=True)
print(pop5.head(10))

pop5 = pop2.sort_values(by="행정구역명", ascending=False)
print(pop5.head(5))

# 즉시 컬럼 생성 방법
pop5['남자인구비율'] = pop5['남자 인구수'] / pop5['총인구수'] * 100
pop5['여자인구비율'] = pop5['여자 인구수'] / pop5['총인구수'] * 100
print(pop5.head(10))
