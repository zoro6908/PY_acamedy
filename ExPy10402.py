# 파이썬 기초부터 활용까지 (2020.09)
# [4과] 제어문1
# if문 : 연습문제
age = input('나이를 입력하시요~~~~ : ')
print('당신의 나이는 : ' + age + '입니다.')

age = int(age)
if age < 5:
    print('당신은 유아에 해당합니다.')
elif age >= 5 and age < 10:
    print('당신은 어린이에 해당합니다.')
elif age >= 10 and age <= 19:
    print('당신은 학생입니다.')
else:
    print('당신은 성인입니다.')