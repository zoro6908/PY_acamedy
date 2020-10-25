# matplotlib 수업
from matplotlib import pyplot as plt, font_manager
import numpy as np
import math

# 한글 폰트 사용하기 위해 설정
# 원도 10에 있는 기본 폰트 파일을 사용하로록 설정하기

import matplotlib.font_manager as fm
import matplotlib

# //원도우에 있는 폰트 파일의 위치를 지정합니다
font_location = "C:\Windows\Fonts\H2MJRE.TTF"

# //폰트 파일의 설정에서 이름정보를 가져 조회합니다
font_name = fm.FontProperties(fname = font_location).get_name()
# // 폰트파일의 이륾을 matplotlib에 설정합니다
matplotlib.rc('font', family = font_name)

# 샘플데이터 - 사원별 월별 실적을 랜텀으로 생성함
np.random.seed(0)
hong = np.ceil(np.random.rand(12) * 100)
kang = np.ceil(np.random.rand(12) * 100)
date = np.arange(1, 13)

# 라인프래프 설정
plt.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(date, hong, label = '홍길동')
ax.plot(date, kang, label = '강감찬')

# 축 제목과 범례 그리기
# ax.set_title('영업 사원별 월별 실적', fontproperties = font)
# ax.set_ylabel('실적(단위 : 원)', fontproperties = font)
# ax.set_xlabel('월', fontproperties = font)
ax.legend()
plt.show()