# [직딩잇템]업무를 쉽게 만드는 실용적인 파이썬 활용법(2020.12)
# 5 차시 : 파일 및 폴더 위치와 이름 변경하기
# basic.py

# -*- coding: utf-8 -*-

import os

def main():
    # os 하위에 있는 path 모듈의 isfile 메소드를 사용해서, 파일의 존재 유무를 검사합니다.
    # 또, os 하위에 있는 rename 메소드를 사용해서, 파일의 이름을 변경합니다.
    if os.path.isfile('./sample'):
        os.rename('./sample', './SAMPLE')


if __name__ == '__main__':
    main()
