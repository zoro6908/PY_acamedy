# 파이썬 기초부터 활용까지 (2020.09)
# [8과] 함수(function) 1

# 본체와 함수간 데이터 흐름
# 인수의 기본값 : 호출쪽에서 인수를 넘겨주지 않을 때 설정될 기본 값
def incre(data, interval = 1):
    data += interval
    return data

a = 100; b = 100
a = incre(a); print(a)        # 인수 없이 호출 : 101

a = incre(a, 10); print(a)    # 인수를 넣어서 호출 : 111
a = incre(b, 10); print(a)    # 인수를 넣어서 호출 : 110

def find(source, ch, all = False):
    position = [ ]
    for i in range(len(source)):
        if source[i] == ch:
            position.append(i)
            if not all:
                break
    return position

s = '배구 우리나라 우생순 우승'

k = find(s, '우'); print(k)           # [3]
k = find(s, '우', True); print(k)     # [3, 8, 12]

# 함수를 호출할 때 인수 이름(key word)을 통해 값을 전달
def printing(source, repetition = 1):
    for i in range(repetition):
        print(source)

printing('korea')
printing(repetition=5, source="china")