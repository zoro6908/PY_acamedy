# 파이썬 기초부터 활용까지 (2020.09)
# [7과] file로 부터 읽고 쓰기

# pickle 모듈
# 구조화된 객체를 파일에 저장 및 복원해 주는 모듈, 문자열로의 변호ㅘ 등의 절차가 필요 없다
# pickliing : 객체가 저장되기 위해 바이트 스트링으로 변화되는 과정 (object serialization)
# unpickliing : 바이트 스트링에서 원본객체로 복원되는 과정 (object deserialization)
####################################################################################
# 저장 작업
# 1단계 : 피클모듈 임포트 : import pickle
# 2단계 : 파일오픈 : f = open('파일명', w)
# 3단계 : 데이터 저장 : pickle.dump(데이터, f)
# 4단계 : 파일 클로징 : f.close()
####################################################################################
# 읽기 작업
# 1단계 : 피클모듈 임포트 : import pickle
# 2단계 : 파일오픈 : f = open('파일명', r)
# 3단계 : 데이터 읽기 : data = pickle.loda(f)
# 4단계 : 파일 클로징 : f.close()
####################################################################################

import pickle

myDic = {'김':'02-3250', '박':'032-3444'}
myLst = [24, 56, 98]
myStr = ' beautiful country~~~'

# f = open('ExPy10704.txt', 'wb', encoding='UTF8')   # ValueError: binary mode doesn't take an encoding argument
f = open('ExPy10704.txt', 'wb')                      # 바이너리로 저장되므로 인코딩 필요없음
pickle.dump(myDic, f); pickle.dump(myLst, f); pickle.dump(myStr, f)
f.close()

f = open('ExPy10704.txt', 'rb')
data1 = pickle.load(f); data2 = pickle.load(f); data3 = pickle.load(f)
f.close()

print(data1)                  # {'김': '02-3250', '박': '032-3444'}
print(data2)                  # [24, 56, 98]
print(data3)                  #  beautiful country~~~

print(data1['박'])            # 032-3444
print(data2[1])               # 56

# 비교
dt1 = {'김':34, '박':56}
dt2 = str(dt1)
print(dt2)

f = open('ExPy10705.txt', 'w')
f.write(dt2)
f.close()

f = open('ExPy10705.txt', 'r')
dt3 = f.read()
print(dt3)
dt3 = eval(dt3)
print(dt3['박'])