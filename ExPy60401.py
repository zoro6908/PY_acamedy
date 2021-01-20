# 빅데이터 수집을 위한 파이썬 웹 크롤링 (2021.01)

# [ 4 차시 ] HTML문서를 BeautifulSoup으로 검색하기
# 연습자료

from bs4 import BeautifulSoup

page = open('c:\\Temp\\sample.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify())                          # 전체 파싱한 자료를 이쁘게 출력
# print(soup.find_all('p'))                       # 전체 p태그
# print(soup.find('p'))                           # 첫번쟤 p태그

# <p class='outer-text>
# print(soup.find_all('p', class_='outer-text'))  # p태그 중에서 class 속성이 outer-text인 것만, 'calss_' 주의
# print(soup.find_all('p', id='first'))           # p태그 중에서 id 속성이 firste인 것만
# print(soup.find_all('p').get_text())            # AttributeError: ResultSet object has no attribute 'get_text'.
# print(soup.find('p').get_text())                # 첫번쨰 p태그의 text 가져오기

for tag in soup.find_all('p'):                  # 반복문을 이용하하여 p태그를 가지 데이터의 text 가져오기
    print(tag.get_text())

