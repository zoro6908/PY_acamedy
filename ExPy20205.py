# 파이썬을 활용한 데이터 분석 및 시각화 [3과]
# 연습문제 DataFrame 데이터 베이스 연결 : DB파일이 같은 폴더에 있어야 함
import pandas as pd
import sqlite3

con = sqlite3.connect("test.db")
df = pd.read_sql("SELECT * FROM sales", con)

print(df)

# SQLite3 DB로 저장하기
# con = sqlite3.connect("test.db")
# df1 = pd.DataFrame({'itemnum' : [4, 5, 6],
#                     'itemname' : ['감자칩', '꼬깔콘', '초코파이'],
#                     'salesqty' : [2, 3, 4],
#                     'salesamount' : [1000, 2000, 1500]})
# df1.to_sql("sales", con, if_exists="append", index=False)

con.close()