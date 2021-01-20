# ExPy9xxxx 파이썬 개인 연습

# pandas를 이용한 NCP 가격 정보 저장

import pandas as pd

# 웹 사이트에서 페이지를 가져오기 위한 라이브러리 입니다.
import requests

# 웹 사이트에 요청을 보낼때, URL Encoding 을 하기 위한 라이브러리 입니다.
from urllib.parse import quote

# 받아온 웹 페이지의 HTML 정보를 분석(파싱)하기 위한 라이브러리 입니다.
from bs4 import BeautifulSoup

# 검색할 구글의 URL 입니다.
# - tbm 은 검색할 분야를 선택하는 부분으로 예제에서는 뉴스를 검색하기 위해 nws 로 설정했습니다.
# - q 는 검색할 단어를 입력하는 부분으로 예제에서는 '컴퓨터' 로 지정했습니다.
# SEARCH_URL = "https://www.google.co.kr/search?tbm=nws&q=%s"

def main():
    # User-Agent 값을 추가하기 위한 부분으로 홈페이지로 정보를 요청하는 부분이 크게 Header 와 Body 로
    # 이루어지는데, 이 중에서 Header 에 내용을 첨부합니다.
    # 특정 웹 사이트에서는 이 설정이 되어있지 않으면, Bot 으로 인식해서 데이터를 전달해주지 않습니다.
    # Uesr-Agent 값은 강의 영상에 나와있듯이 일반적인 브라우저에서 Uesr-Agent 값을 조회해서 사용하면 됩니다.
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' }

    # 검색어를 입력하는 부분으로 quote 메소드를 사용해서, 한글을 URL Encoding 합니다.
    # search_keyword = quote("컴퓨터")
    # URL Encoding 된 데이터를 SEARCH_URL 에 포함시켜 검색할 URL 을 만듭니다.
    # url = SEARCH_URL % search_keyword

    url = 'https://www.ncloud.com/charge/region/ko'


    # 검색할 URL 과 header 를 requests 의 get 의 인자로 전달해서 결과를 요청합니다.
    response = requests.get(url, headers=headers)

    # 검색의 결과는 HTML 형태로 반환되는데, BeautifulSoup 모듈을 사용해서 결과를 분석(파싱) 합니다.
    # BeautifulSoup 에서 HTML 을 분석할 때, 여러가지 parser 를 사용할 수 있는데, 그중에서 html5lib 파서를 사용합니다.
    soup = BeautifulSoup(response.text, "html5lib")

    # 크롬 브라우저의 '검사' 기능을 사용해서 selector 값을 추출합니다.
    # 추출한 selector 값을 사용해서, 원하는 부분을 추립니다.
    # 예제에서는 기사의 제목을 추리는데에 사용했습니다.
    # 실제로는 제목만 추리는 것이 아니라, 제목과 관련된 HTML 태그의 데이터도 함께 추출됩니다.
    # titles = soup.select("#rso > div > div > div > div > h3 > a")
    titles = list()

    # for i in range[1:82]:
    #     titles = soup.select('#app > article > div.price-detail > ul > li:nth-child(' + str(i) + ') > h3')
    titles = soup.select('#app > article > div.price-detail > ul > li:nth-child(1) > h3')
    print(titles, type(titles))
    # app > article > div.price-detail > ul > li:nth-child(1)

    # # selector 로 추린 제목의 목록을 순회하며, 제목과 관련된 기사의 링크를 추출합니다.
    # for title in titles:
    #     subject = title.text
    #     # HTML 의 a 태그의 속성인 href 를 이용하여, 기사 제목에 포함된 본문 링크를 추출합니다.
    #     link = title.get("href")
    #     print ("%s\n - %s" % (subject, link))


if __name__ == '__main__':
    main()





#
#
#
#
#
#
# name1 = ['df0', 'df1', 'df2', 'df3', 'df4', 'df5', 'df6', 'df7']
#
# titles = app > article > div.price-detail > ul > li:nth-child(1) > h3
#
# with pd.ExcelWriter('ExPy90112_ncp_server.xlsx') as writer:
#     for i in range(8):
#         name = pd.read_html('https://www.ncloud.com/charge/region/ko', header=0)[i]
#         name.to_excel(writer, sheet_name=name1[i])
#
# #app > article > div.price-detail > ul > li:nth-child(1) > h3
# #app > article > div.price-detail > ul > li:nth-child(2) > h3
# #app > article > div.price-detail > ul > li:nth-child(81) > h3
#
# #app > article > div.price-detail > ul > li:nth-child(1) > div > div > ul > li:nth-child(1)
# #app > article > div.price-detail > ul > li:nth-child(1) > div > div > ul
#
# # name[0].to_excel('ExPy90112_ncp_server0.xlsx')
# # name[1].to_excel('ExPy90112_ncp_server1.xlsx')
# # name[2].to_excel('ExPy90112_ncp_server2.xlsx')
# # name[3].to_excel('ExPy90112_ncp_server3.xlsx')
# # name[4].to_excel('ExPy90112_ncp_server4.xlsx')
# # name[5].to_excel('ExPy90112_ncp_server5.xlsx')
# # name[6].to_excel('ExPy90112_ncp_server6.xlsx')
# # name[7].to_excel('ExPy90112_ncp_server7.xlsx')
# # app > article > div.price-detail > ul > li:nth-child(2) > h3
