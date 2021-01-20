# [직딩잇템]업무를 쉽게 만드는 실용적인 파이썬 활용법(2020.12)
# 4 차시 : 파일 내용 다루기
# use_with.py

# -*- coding: utf-8 -*-

def use_read():
    # with 구문을 사용해서, 코드를 간단히 바꿀 수 있습니다.
    # close 구문을 생략하고, 사용할 수 있습니다.
    with open('c:/Temp/ExPy40000/test_file', 'r') as f:
        print(f.read())

def use_readline():
    with open('c:/Temp/ExPy40000/test_file', 'r') as f:
        while True:
            line = f.readline()

            if not line:
                break

            print(line)

def use_readlines():
    with open('c:/Temp/ExPy40000/test_file', 'r') as f:
        print(f.readlines())

def use_write():
    with open('c:/Temp/ExPy40000/write_test', 'w') as f:
        f.write('python3\n')
        f.write('write test\n')

def use_write_with_append():
    with open('c:/Temp/ExPy40000/write_test', 'w') as f:
        f.write('appended line\n')

def main():
    use_read()
    print ('================')
    use_readline()
    print ('================')
    use_readlines()


if __name__ == '__main__':
    main()
