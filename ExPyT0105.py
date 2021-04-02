# 파이썬 웹 스크랭핑 강의 3
# https://nadocoding.tistory.com/10

# user agent : 확인 구글에서 'user agent string' 이라 치고 'what is my user agent' 가면 나옴
# 무제한 젭속이나 기기를 사용하지 않는 사용 접속을 막기 위해 사용

import requests

url = 'https://nadocoding.tistory.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

# res = requests.get(url)
res = requests.get(url, headers=headers)

res.raise_for_status()                         # 에러가 발생되면 에러코드 생성후 프로그램을 끝낸다
# 파일로 만들기
# with open('mygoogle.html', 'w', encoding='utf-8') as f:
#     f.write(res.text)
