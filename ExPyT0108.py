# 파이썬 웹 스크랭핑 강의 6
# https://nadocoding.tistory.com/10
# 쿠팡 노트북 데이터 가져오기

# HTTP METHOD : GET, POST
# GET : 어떤 내용을 누구나 볼수 있게 url을 통해서 보내는 방식
# https://www.coupang.com/np/search?maxPrice=&priceRange=&filterType=&listSize=36&page=1
# 물음표 뒹에 있는 것들로 부터 변수와 값을 표현, 변수와 값은 & 표시로 구분, 개수의 제한이 있음
# POST : url이 아닌 HTTP 바디에 숨겨 보내는 방식
# 파일일나 큰 데이터, 아이디 패스워드등 개인정보 전송방식에 용이

import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

for i in range(1, 6):
    print('페이지 :', i)
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP' \
          '&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36' \
          '&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false' \
          '&searchIndexingToken=1=4&backgroundColor='.format(i)

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', attrs={'class':re.compile('^search-product')})
    print(items[0].find('div', attrs={'class':'name'}).get_text())

    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find('span', attrs={'class': 'ad-badge-text'}).get_text()

        if ad-badge:
            print('   <광고 상품은 제외합니다.>')
            continue

        name = item.find('div', attrs={'class':'name'}).get_text()

        # 애플 제품 제외
        if 'Apple' in name:
            print('   <Apple 상품은 제외합니다.>')
            continue

        price = item.find('strong', attrs={'class':'price-value'}).get_text()

        # 리뷰 50개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find('em', attrs={'class':'rating'})
        if rate:
            rate = rate.get_text()
        else:
            # rate = '평점 없음'
            print('   <평점 없는 상품은 제외합니다.>')
            continue

        rate_count = item.find('span', attrs={'class':'rating-total-count'}).get_text()
        if rate_count:
            rate_count = rate_count.get_text()  # 예 : (26)
            rate_count = rate_count[1:-1]
        else:
            # rate_count = '평점 수 없음'
            print('   <평점 수 없는 상품은 제외합니다.>')
            continue

        link = item.find('a', sttrs={'class':'search-product-link'})['href']

        if float(rate) >= 4.5 and int(rate_count) >= 50:
            # print(name, price, rate, rate_count)
            print(f'제품명 : {name}')
            print(f'가격 : {price}')
            print(f'평점 : {rate}점, ({rate_count}개)')
            print('바로가기 : {}'.format('https://www.coupang.com' + link))
            print('-'*100) # 줄긋기
