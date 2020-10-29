# 파이썬 기초부터 활용까지 (2020.09)
# [7과] file로 부터 읽고 쓰기

# 파일 작업시 일반적인 업무순서
# 1단계 : file 핸들러 객체를 생성한다 : f = open('test.txt', 'r'); f2 = open('test.text., 'w')
# 2단계 : file 핸들러를 이용하여 읽거나 쓰기 작업을 한다 : my_data = f.read(); f2.write(mydate)
# 3단계 : file 핸들러를 닫아 준다 : f.close(); f2.close()

# f = open('ExPy10701.txt', 'r')
# data = f.read() # UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 0: illegal multibyte sequence
# print(data)

f = open('ExPy10701.txt', 'r', encoding='UTF8')
data1 = f.read()
print(data1)

data2 = data1.split('\n')
print(data2)                 # ['나 보기가 역겨워', '가실 때에는', '말없이 고이 보내드리우리다', ... ]

f.close()

# 한줄 읽기 메서드 : readline(), 한꺼번에 일기(파일포인터) : readlines()
f = open('ExPy10701.txt', 'r', encoding='UTF8')
data3 = f.readline(); print(data3)   # 나 보기가 역겨워
data4 = f.readline(); print(data4)   # 가실 때에는 : 파일 포인터가 옭겨져 그 다음줄을 읽어옴
data5 = f.readlines(); print(data5)  # [말없이 고이 보내드리우리다\n', '영변에 약산\n'... ]

f.close()

# for문 이용
f = open('ExPy10701.txt', 'r', encoding='UTF8')
data6 = f.read()
for line in data6:
    print(line, end='')
f.close()
