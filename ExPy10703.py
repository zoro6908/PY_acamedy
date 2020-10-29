# 파이썬 기초부터 활용까지 (2020.09)
# [7과] file로 부터 읽고 쓰기

# 응용문제 : 성적프로그램 파일 버전 만들기

a = '''김영민, 69, 100, 100
박동식, 100, 98, 98
최민규, 88,96, 90
기동민, 88, 98, 87
이홍걸, 99, 44, 66
김철규, 88, 69, 100'''

data = a.split('\n')                    # 줄바꿈 분리
data = list(data)                       # 리스트 유형으로 변화
# print(type(data)); print(data)

for ele in range(len(data)):
    data[ele] = data[ele].split(',')    # 콤마로 분리하여 인원별 재할당 --> 중첩리스트
# print(data)

# f = open('ExPy10703.txt', 'w', encoding='UTF8')
# for i in range(len(data)):              # 인원수 만큼 반복
#     sum = 0
#     for j in range(1, len(data[i])):    # 과목수 만큼 반복
#         data[i][j] = int(data[i][j])
#         sum = sum + data[i][j]          # 세과목 합계
#     data[i].append(sum)                 # 각 인원별 합계 리스트에 추가
#     av = int(sum / 3)
#     data[i].append(av)                  # 각 인원별 평균 리스트에 추가
#     data1 = ', '.join(data[i]) + '\n'   # TypeError: sequence item 1: expected str instance, int found
#
#     f.write(data1)
# # print(data)
# f.close()

f = open('ExPy10703.txt', 'w', encoding='UTF8')
for i in range(len(data)):              # 인원수 만큼 반복
    sum = 0
    for j in range(1, len(data[i])):    # 과목수 만큼 반복
        data[i][j] = int(data[i][j])
        sum = sum + data[i][j]          # 세과목 합계
        data[i][j] = str(data[i][j])    # [소스 바꿈] str로 바꾸어야 나중에
    data[i].append(str(sum))            # 각 인원별 합계 리스트에 추가 : # [소스 바꿈] str로 바꾸어야 나중에
    av = int(sum / 3)
    data[i].append(str(av))             # 각 인원별 평균 리스트에 추가 : # [소스 바꿈] str로 바꾸어야 나중에
    data1 = ', '.join(data[i]) + '\n'

    f.write(data1)
# print(data)
f.close()