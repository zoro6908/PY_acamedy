# 파이썬 기초부터 활용까지 (2020.09)
# [4과] 제어문1
# while문 : 조건이 참인 동안 특정 문장들을 반복적으로 수행 (거짓 혹은 break를 만날 때까지)
# cf : if문은 한번만 수행
# while True: print('ttttt')    # 무한 루프

# 연습문제 : 1에서 10까지 합을 구하는 프로그램
n = 0
sum = 0
while n < 10:
    n = n + 1
    sum = sum + n
    print(n, '.. 까지 합은...', sum)
    # print(str(n) + '.. 까지 합은...' + str(sum))  # + 는 string 결합만 가능 아니면 Errror


