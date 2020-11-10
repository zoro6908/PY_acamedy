# 파이썬 기초부터 활용까지 (2020.09)
# [10과] 튜플과 딕션너리

# 응용 실습 : 전화번호부 구현하기
def read_from_file():
    global telDic
    f = open('ExPy11004.txt', 'r', encoding='UTF8')
    basedata = f.read()
    f.close()

    data = basedata.split('\n')
    telDic = {}

    for i in range(len(data)):
        person = data[i].split(',')
        telDic[person[0]] = person

def printing():
    print('\n\n                         전화번호 목록')
    print('-------------------------------------------------------------------------')
    print('이름     전화번호     주소                소속사')
    print('-------------------------------------------------------------------------')

    for k in telDic:
        print('{} ----> {:15s} {:15s} {:10s}'.format(k, telDic[k][1], telDic[k][2], telDic[k][3]) )

def main():
    read_from_file()
    printing()

    while True:
        sName = input('\n이름을 입력하세요[끝내려면-->끝 입력] --->  ')
        if sName == '끝':
            print('\n프로그램을 끝냅니다.')
            break

        if sName in telDic:
            print(sName, '--------> ', telDic[sName])
        else:
            print('등록된 전화번호가 없습니다.')

main()
