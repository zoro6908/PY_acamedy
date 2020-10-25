# 응용문제

a = '''김영민, 69, 100, 100
박동식, 100, 98, 98
최민규, 88,96, 90
기동민, 88, 98, 87
이홍걸, 99, 44, 66
김철규, 88, 69, 100'''

# print(a)
# print(type(a))

data =  a.split('\n')
# print(data)
# print(len(b))
# print(type(b))

for i in range(len(data)):
    data[i] = data[i].split(",")

# print(data)

for i in range(len(data)):
    sum = 0
    for j in range(1, 4):
        data[i][j] = int(data[i][j])
        sum = sum + data[i][j]
    data[i].append(sum)
    av = int(sum/3)
    data[i].append(av)
    # print(data[i])

data.sort(key=lambda a: a[4], reverse=True)
# for i in range(len(data)):
#     print(data[i])

for i in range(len(data)):
    data[i].append(1)
    # print(data[i])

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i][4] < data[j][4]:
            data[i][6] += 1
        elif data[i][4] > data[j][4]:
            data[j][6] += 1
    # print(data[i])

print('        성적 처리 결과        ')
print('-----------------------------')
print('{0:4s} {1:2s} {3:2s} {4:2s} {5:2s} {6:2s}'.format('이름', '국어', '영어', '수학', '총점', '평균', '석차'))
print('-----------------------------')

for i in range(len(data)):
    print('{0:4s} {1:3d} {3:3d} {4:4d} {5:3d} {6:3d}'.format(data[i][0], data[i][1], data[i][2],
                                                             data[i][3], data[i][4], data[i][5], data[i][6]))



