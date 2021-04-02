# 파이썬 웹 스크랭핑 강의 9
# https://nadocoding.tistory.com/10
# 네이버 항공권 조회
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()      # 창 최대화

url ='https://flight.naver.com/flights/'
browser.get(url)               # url로 이동

# 가는 날 선택
browser.find_element_by_link_text('가는날 선택').click()

# # 이번달 27, 28일 선택
# browser.find_elements_by_link_text('27')[0].click()  #[0] 이번달 (첫번쨰)
# browser.find_elements_by_link_text('28')[0].click()  #[0] 이번달 (첫번쨰)
# # 다음달 27, 28일 선택
# browser.find_elements_by_link_text('27')[1].click()  #[1] 다음달 (두번쨰)
# browser.find_elements_by_link_text('28')[1].click()  #[1] 다음달 (두번쨰)
# 이번달 27, 다음달28일 선택
browser.find_elements_by_link_text('27')[0].click()  #[0] 이번달 (첫번쨰)
browser.find_elements_by_link_text('28')[1].click()  #[1] 다음달 (두번쨰)

# 제주도 선택
# 다른 태그에 숨겨 위치를 못찾을 떄는 다른 태그를 이용한다:
# browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div/a').click()
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 로딩시간을 기다려 주기 위해서
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    # 성공했을 떄 동작을 수행
    print(elem.text)      # 첫번쨰 결과 출력
finally:
    browser.quit()

# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)

