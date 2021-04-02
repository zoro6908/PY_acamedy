# 파이썬 웹 스크랭핑 강의 11
# https://nadocoding.tistory.com/10
# 동적 페이지에 대한 웹스크래핑, 구글 무비
# 백그라운드로 크롬 실행 : headless Chrome
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('winddow-size=1920x1080')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://play.google.com/store/movies/top'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
           'Accept-Language':'ko-KR,ko'}

# 페이지 이동
browser.get(url)

# 지정한 위치로 스크롤 내리기 (1080만큼)
# browser.execute_script('window.scrollTo(0, 1080)')  # 내 피씨 해상도 : 1920 X 1080
# 화면 가장 아래로 스크롤 내리기
# browser.execute_script(window.scrollTo(0, document.body.scrollHeight))

import time
interval = 2  # 2초에 한번씩 스코롤릉 내림

# 현재의 문서높이를 가져와 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재의 문서높이를 가져와 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height:
        break

    prev_height = curr_height

print('스크롤 완료')

browser.get_screenshot_as_file('googile_movie.png')

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

# movies = soup.find_all('div', attrs={'class':'ImZGtf mpg5gc'})
# movies = soup.find_all('div', attrs={'class':['ImZGtf mpg5gc', 'Vpfmgd']})
movies = soup.find_all('div', attrs={'class':'Vpfmgd'})
print(len(movies))

# with open('google_movie.html', 'w', encoding='utf8') as f:
#     # f.write(res.text)
#     f.write(soup.prettify())  # html을 예쁘게 출력
for movie in movies:
    title = movie.find('div', attrs={'class':'WsMG1c nnK0zc'}).get_text()
    # 할인전 가격
    orignal_price = movie.find('span', attrs={'class':'SUZt4c djCuy'})
    if orignal_price:
        orignal_price = orignal_price.get_text()
    else:
        continue

    # 할인된 가격
    price = movie.find('span', attrs={'class':'VfPpfd ZdBevf i5DZme'}).get_text()

    # 링크
    link = movie.find('a', attrs={'class':'JC71ub'})['href']

    # 올바른 링크 https://play.google.com/ + link
    print(f'제목 : {title}')
    print(f'할인전 가격 : {orignal_price}')
    print(f'할인된 가격 : {price}')
    print('링크 :', 'https://play.google.com/' + link)
    print('-' * 80)

browser.quit()