# 파이썬을 활용한 데이터 분석 및 시각화 (2020.10)
#
# 7 차시 : Konlpy를 활용한 한글 텍스트 분석 및 시각화
################################################
# 텍스트 분석 순서
# 문장 -> 단어 -> 키워드 -> 필터링 -> 집계 -> 시각화
################################################
# konlpy 패캐지 인스톨 필요 : 한글분석에 특화된 패키지 : korean natural languge
# konlpy 및 wordcloud 패캐지 인스톨 필요

# Step1 필요한 모듈을 실행
from konlpy.tag import Kkma
import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc
from wordcloud import WordCloud
from collections import Counter
import numpy as np

kkma = Kkma()                     # 꼬고마 사전 함수 : 문장을 입력받아 형태소 분석해서 명사를 골라내줌

# Step2 파일을 불러와서 형태소 분석
source = open('c:\\Temp\\경주여행_지식인_2016_2.txt').read()
# print(source)
data2 = kkma.nouns(source)        # 명사만 골라냄
# print(data2)

# f = open('ttt.txt', 'w', encoding='utf-8')
# s = ''
# for a in data2:
#     s = s + str(a) + '\n'
# f.write(s)
# f.close()
data3 = Counter(data2)

# Step3 불용어 제거
stopwd = open('c:\\Temp\\stop_words.txt').read()
data3 = [ each_word for each_word in data2 if each_word not in stopwd ]

data4 = list()
# 1글자이하이거나 10글자이상인 것은 삭제 : 띠어쓰기 기준으로 단어를 판단하므로 글자수의 제약이 필요
for i in range(0, len(data3)):
    if len(data3[i]) >=2 | len(data3[i]) <= 10:
        data4.append(data3[i])

# Step4 단어별 빈도수 집계
data5 = Counter(data4)
data6 = data5.most_common(100)      # 가장 많이 언급된 100개
tmp_data = dict(data6)

# Step5-1 워드 클라우드 그리기 : 한글폰트 지원이 안됨
wordclound = WordCloud(font_path='c:\\windows\\fonts\\NanumGothic.ttf',
                       relative_scaling=0.2,
                       background_color='black').generate_from_frequencies(tmp_data)
plt.figure(figsize=(8,4))
plt.imshow(wordclound)
plt.axis('on')
plt.show()

# Step5-2 워드 클라우드 그리기 : 한글폰트 지원이 안됨
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

alice_mask = np.array(Image.open('c:\\Temp\\alice.jpg'))
wc = WordCloud(font_path='c:\\windows\\fonts\\NanumGothic.ttf',
               relative_scaling=0.2,
               mask=alice_mask,
               background_color='white',
               min_font_size=1,
               max_words=2000).generate_from_frequencies(tmp_data)
plt.figure(figsize=(8,8))
plt.imshow(wc)
plt.axis('off')
plt.show()

# 그래프로 그리기
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib
# import matplotlib.rc as rc

# font_location = 'C:\\Windows\\Fonts\\gulim.ttc'
# font_name = fm.FontProperties(fname=font_location).get_name()
# matplotlib.rc('font', family='font_name')

import nltk
plt.figure(figsize=(20,4))

from nltk.probability import FreqDist
g_data4 = FreqDist(data3)

g_data4.plot(50)



