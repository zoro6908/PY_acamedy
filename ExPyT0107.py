# 파이썬 웹 스크랭핑 강의 5
# https://nadocoding.tistory.com/10
# 가우스 전자 만화 목록

import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all('td', attrs={'class':'title'})
# print(cartoons)
title = cartoons[0].a.get_text()
link = cartoons[0].a['href']
print(title)
print('https://comic.naver.com' + link)

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     print(cartoon.a.get_text(), 'https://comic.naver.com' + cartoon.a['href'])

# 평점 가져오기
# total_rate = 0
# cartoons = soup.find_all('div', attrs={'class':'rating_type'})
# for cartoon in cartoons:
#     rate = cartoon.find('strong').get_text()
#     print(rate)
#     total_rate += float(rate)
# print('전체 점수 :', total_rate)
# print('평균 점수 : ', total_rate / len(cartoons))