# 파이썬 웹 스크랭핑 강의 9
# https://nadocoding.tistory.com/10
# 네이버 로그인
# chromdriver 설치
# selenium 패캐지 인스톨
from selenium import webdriver
import time

browser = webdriver.Chrome()  # './chromedriver.exe'

# 네이버로 이동
browser.get('http://naver.com')

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 아이디, 패트워드 입력
elem = browser.find_element_by_id('id').send_keys('naver_id')
elem = browser.find_element_by_id('pw').send_keys('naver_pw')

# 로그인 버큰 클릭
browser.find_element_by_id('log.login').click()

# time.sleep(3)

# 아이디를 새로 입력
browser.find_element_by_id('id').clear()    # 이전의 입력된 값을 지워줌
browser.find_element_by_id('id').send_keys('my_id')

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
# browser.close()  # 현재 탭만 종료
browser.quit()   # 전체 브라우저 종료