f = open('temp1.txt', 'r', encoding='UTF8')
data1 = f.read()
data2 = data1.split('\n\n')
# data3 = data2.split(',')
print(type(data1), type(data2))
print(data2)

for ele in range(len(data2)):
    # data2[ele] = data2[ele].split(':', ',')
    data2[ele] = data2[ele].split(',')    # 콤마로 분리하여 인원별 재할당 --> 중첩리스트
print(data2)

wf = open('temp2.txt', 'w', encoding='UTF8')

for i in range(len(data2)):
    for j in range(len(int(data2[i]))):
        data2 = ', '.join(data2[i]) + '\n'
        wf.write(data2)

f.close()
# f1.close()