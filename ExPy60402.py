# 빅데이터 수집을 위한 파이썬 웹 크롤링 (2021.01)

# [ 4 차시 ] HTML문서를 BeautifulSoup으로 검색하기
# 강의 제공 자료 web02.py

from bs4 import BeautifulSoup
# page = open('sample.html', 'rt', encoding='utf-8').read()

page = open('c:\\Temp\\sample.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())

# 문서 내부에 있는 <p>태그를 모두 검색합니다.
# print(soup.find_all('p'))

# <p>태그 하나만 검색합니다.
# print(soup.find('p'))

# <p>태그 중에 class="outer-text"만 검색합니다.
# print(soup.find_all('p', class_='outer-text'))

# 태그를 지정하고 지정하지 않고 class="outer-text"인 경우를 검색합니다.
# print(soup.find_all(class_='outer-text'))

# 태그의 id속성이 id="first"인 경우를 검색합니다.
# print(soup.find_all(id='first'))

# <p>태그를 찾아서 내부의 문자열만 출력합니다.
for tag in soup.find_all('p'):
    print(tag.get_text())
