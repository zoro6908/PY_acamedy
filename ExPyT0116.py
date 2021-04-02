# 파이썬 웹 스크랭핑 강의 11
# https://nadocoding.tistory.com/10
# 동적 페이지에 대한 웹스크래핑, 구글 무비
# 백그라운드로 크롬 실행 : headless Chrome
# selenium을 더 공부하고 싶으면 : selenium with python 을 검색

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('winddow-size=1920x1080')

# headless 없애주는 agent를 받아오기 위해서는
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)
detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/88.0.4324.150 Safari/537.36