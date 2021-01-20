# ExPy9xxxx 파이썬 개인 연습
# MySQL 연결
# 선행작업 : PyMySQL 패키지 install

import pymysql

con = pymysql.connect(
    user = 'root',
    passwd = 'zoro123',
    host = '127.0.0.1',
    db = 'testdb',
    charset = 'utf8'
)

# 딕셔너리 형태로 결과를 반환해주는 DictCursor를 사용
cursor = con.cursor(pymysql.cursors.DictCursor)

# Insert
# sql = '''INSERT INTO `user` (userID, userPassword, userName, userGender, userEmail )
#     VALUES ('1', '1', 'kim', '여자', 'femail@aa.aaa');'''
#
# cursor.execute(sql)
# con.commit()

# Update
# sql = '''UPDATE `user` SET userName = 'jung', userGender = '여자'
#      WHERE userID = '111';'''
#
# cursor.execute(sql)
# con.commit()

# Delete
sql = '''DELETE FROM `user` WHERE userID = 'zoro2';'''

cursor.execute(sql)
con.commit()

# 조회
sql = 'SELECT * FROM user;'
cursor.execute(sql)
result = cursor.fetchall()
# fetchall()	모든 데이터를 한 번에 가져올 때 사용
# fetchone()	한 번 호출에 하나의 행만 가져올 때 사용
# fetchmany(n)	n개 만큼의 데이터를 가져올 때 사용


import pandas as pd

df = pd.DataFrame(result)

print(df)

# import openpyxl as xl

df.to_excel('ExPy90101.xlsx', index=False)

# wb = xl.Workbook()
# ws = wb.active
#
# for i in range(len(result)):
#     for j in range(len(result[i])):
#         ws.cell(i, j).value = j[i][j]
#
# wb.save('ExPy90101.xlsx')
