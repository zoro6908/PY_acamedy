# [직딩잇템]업무를 쉽게 만드는 실용적인 파이썬 활용법(2020.12)
# 5 차시 : 파일 및 폴더 위치와 이름 변경하기
# 활용 파일 이름, 크기 가져오기

import os
import glob
import pandas as pd

path = 'c:/Movie'

lst = glob.glob('c:\Movie\**', recursive=True)

size = list()
name = list()
dir = list()
extension = list()

for filename in lst:
    if filename.endswith('mp4') or filename.endswith('avi') or filename.endswith('mkv'):
        size.append(os.path.getsize(filename))
        name.append(os.path.basename(filename))
        dir.append(os.path.dirname(filename))
        extension.append(os.path.splitext(filename)[1][1:])

df = pd.DataFrame([ x for x in zip(dir, name, extension, size)])

df.to_excel('ExPy40591.xlsx')