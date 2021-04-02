# 파이썬 웹 스크랭핑 강의 7
# https://nadocoding.tistory.com/10
# 다음 영화 이미지 가져오기
import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

    res = requests.get(url=url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img', attrs={'class': 'thumb_img'})

    for idx, image in enumerate(images):
        # print(image['src'])
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:' + image_url
        print(image_url)

        image_res = requests.get(url=image_url)
        image_res.raise_for_status()

        with open('move_{}_{}.jpg'.format(year, idx+1), 'wb') as f:
            f.write(image_res.content)

        if idx >= 4:  # 상위 5개만 받아오기
            break
