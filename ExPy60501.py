# 빅데이터 수집을 위한 파이썬 웹 크롤링 (2021.01)

# [ 5 차시 ] HTML문서를 BeautifulSoup과 re모듈을 사용해서 검색하기
# 연습자료

from bs4 import BeautifulSoup
doc = ['<html><head><title>Page title</title></head>', \
    '<body><p id="firstpara" align="center">This is paragraph <b>one</b></p>', \
    '<p id="secondpara" align="blah">This is a paragraph <b>two</b></p>', '</html>']

soup = BeautifulSoup(''.join(doc), 'html.parser')    # join()을 이용하여 합쳐서 html로 검색이 용이한 객체 만들기
# print(soup.prettify())                               # prettify()로 태그를 정렬하여 보여주기

import re
# tagsStartingWithB = soup.find_all(re.compile('^b'))  # re 모듈 활용
# print([tag.name for tag in tagsStartingWithB])       #

# print(soup.find_all(['title', 'p']))                 # title 태그와 p 태그를 list를 나열하여 검색하기

# print(soup.find_all(lambda tag:len(tag.attrs)==2))   # lambda 함수를 이용하여 속성이 2개가 있는 것만 가져오기
# print(soup.find_all(id=re.compile('para$')))         # re의 compile 함수를 이용하여 id가 para로 끝나는 패턴만 가져오기

soup =BeautifulSoup("""
    Bob's<b>Bold</b>Barbeque Sauce now available 
    <b class="hickory">Hickory</b> and <b class="lime">Lime</a>
    """, "html.parser")

print(soup.find('b', {'class':'lime'}))             # find()를 이용하여 class 속성이 lime 인것 만 지정하여 검색
print(soup.find('b', {'class':'lime'}).get_text())  # find()를 이용하여 원하는 콘텐츠만 검색하기