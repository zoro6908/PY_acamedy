# 파이썬 기초부터 활용까지 (2020.09)
# [5과] 제어문2

# try문 : 예외 처리 문장
# 문법 --> try: A except: B else: C finally D
# 수행문 A를 수행하다가 예외발생시 B 수행, 예외 없을시 C수행, 예외외 관계 없이 D 수행
import sys
while True:
    a = input('\n첫번 째 값을 입력하세요?.....')
    b = input('\n두번 째 값을 입력하세요?.....')

    try:
        a = int(a); b = int(b); c = a / b   # 걱정되는 부분
    except:
        e = str(sys.exc_info()[1])
        if 'division by zero' in e:
            print('******************* 0 으로는 나눌 수 없습니다.')
        elif 'invalid literal for int()' in e:
            print('******************* 숫자만 입력해 주세요.')
    else:
        print('나눈 결과는', c, '입니다.')
    finally:
        break
