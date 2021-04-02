# 파이썬 웹 스크랭핑 강의 4
# https://nadocoding.tistory.com/10

import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)                     # soup 객체에서 처음 발결되는 a 엘리먼트의 정보를 출력
# <a href="#menu" onclick="document.getElementById('menu').
# print(soup.a.attrs)               # soup 객체에서 처음 발결되는 a 엘리먼트의 모든 속성 정보를 출력
# {'href': '#menu', 'onclick': "document.getElementById('menu')
# print(soup.a['href'])             # soup 객체에서 처음 발결되는 a 엘리먼트의 href 속성 '값' 정보를 출력
# #menu
# print(soup.find('a', attrs={'class':'Nbtn_upload'}))  # class='Nbtn_upload' 인 a 엘리먼트를 찾아줘~~~
# <a class="Nbtn_upload" href="/mypage/myActivity.nhn" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
# print(soup.find(attrs={'class':'Nbtn_upload'}))       # class='Nbtn_upload' 인 어떤 엘리먼트를 찾아줘~~~
# <a class="Nbtn_upload" href="/mypage/myActivity.nhn" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>

# print(soup.find('li', attrs={'class':'rank01'}))
# rank1 = soup.find('li', attrs={'class':'rank01'})
# print(rank1.a.get_text())
# print(rank1.next_sibling)    # 아무것도 안나옴, 아무것도 안나오면 중간에 뭐가(개행) 들어 갈수 있으므로 다시 합번 시블링
# # print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling     # 이전 형제 엘리먼트 찾기
# print(rank2.a.get_text())
# print(rank1.parent)                                 # 부모 찾기
# rank2 = rank1.find_next_sibling('li')                 # 개항에 상관없이 'li' 엘리먼트를 가진 다음 형제를 찾는다
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())
# print(rank1.find_next_siblings('li'))               # 형제 전체 찾기
# webtoon = soup.find('a', text='고수-2부 132화')
# print(webtoon)
# # <a href="/webtoon/detail.nhn?titleId=662774&amp;no=222" onclick="nclk_v2(event,'rnk*p.cont','662774','4')"

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all('a', attrs={'class':'title'})
# class 속성이 title 인 모든 'a' 엘리먼트를 반화
for cartoon in cartoons:
    print(cartoon.get_text())