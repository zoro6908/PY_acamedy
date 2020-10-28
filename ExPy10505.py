# 파이썬 기초부터 활용까지 (2020.09)
# [5과] 제어문2

# for문 : 반복문의 중첩
for outer in range(4):
    print('***** 외부 루프 *****', outer)
    for inner in range(5, 9):
        print('내부 : ', inner)