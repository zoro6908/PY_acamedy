# 파이썬 웹 스크랭핑 강의 1
# https://nadocoding.tistory.com/10
# 웹 스크래핑 : 웹에서 내가 원하는 부분만 발췌하는 것 :
# 웹 크롤링 : 웹 페이지의 링크를 따라 가면서 모든 내용을 가져 오는 것 : 서점에서 쓸어 담는 것
# 웹 구성 요소 : html(Hyper Text Markup Language) = 뼈대, css = 예쁘게, js = 살아있게
# html : w3school (유명 html 싸이트 )

# xpath : html 의 경로를 알려 주는 것, 어떤 엘리먼트인지 명확하게 지정해 줌,
# ex: 학교/학년/번/학생[2], //*[@학번='1-1-5']
# 부모 / 자식 관계 하위 댑스의 태그, 다음과 이전은 형제(시블링)
# 크롬의 검사 기능을 이용 : 메뉴 맨 왼쪽 버튼을 누른뒤 웹 페이지의 화면을 선택하면 소스로 바로 이동

# 웹 정보를 가져오기 위해 request lib 필요

import requests

res = requests.get('https://www.google.co.kr')
res.raise_for_status()                         # 에러가 발생되면 에러코드 생성후 프로그램을 끝낸다
# print('응답코드 : ', res.status_code)            # 200이면 정산
# if res.status_code == requests.codes.ok:
#     print('정상입니다')
# else:
#     print('오류가 발생했습니다. [에러코드 ', res.status_code, ']')

print(len(res.text))
print(res.text)

# 파일로 만들기
with open('mygoogle.html', 'w', encoding='utf-8') as f:
    f.write(res.text)