# 예제 프로젝트
# 오늘의 날씨 정보 가져오기
# 헤드라인 뉴스 가져오기
# 네이버 IT 정보 뉴스 가져오기
# 해커스 영어 가져오기

import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
           'Accept-Language':'ko-KR,ko'}

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def print_news(idx, title, link):
    print('{}. {}'.format(idx + 1, title))
    print('(링크 : {} )'.format(link))
    print()

def scrape_weather():
    # 네이버 날씨 정보 가져오기
    print('[오늘의 날씨]')
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'

    soup = create_soup(url)

    # 흐림, 어제보다 oo도 높아요
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()
    # 현재 oo C (최저 oo C, 최고 oo C)
    cur_temp = soup.find('p', attrs={'class':'info_temperature'}).get_text().replace('도씨', '') # 현재온도
    min_temp = soup.find('span', attrs={'class':'min'}).get_text() # 최저온도
    max_temp = soup.find('span', attrs={'class':'max'}).get_text() # 최고온도
    # 오전 강수 확률 00% / 오후 강수 확귤 oo%
    morning_rain_rate = soup.find('span', attrs={'class':'point_time morning'}).get_text().strip()
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip()
    # 미세먼지 oo 좋음
    # 초미세먼지 oo 좋음
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm10 = dust.find_all('dd')[0].get_text()    # dd 태그중 1번쪠 것
    pm25 = dust.find_all('dd')[1].get_text()    # dd 태그중 2번쪠 것

    # 출력
    print(cast)
    # print('현재 ', cur_temp, '(최저 ', min_temp, '최고 ', max_temp, ')')
    print('현재 {} (최저 {} 최고 {})'.format(cur_temp, min_temp, max_temp))
    print('오전 {} / 오후 {}'.format(morning_rain_rate, afternoon_rain_rate))
    print()
    print('미세먼지 : {}'.format(pm10))
    print('초미세먼지 : {}'.format(pm25))
    print()

def scrape_headline_news():
    # 네이버 헤드라인 뉴스 가져오기
    print('[헤드라인 뉴스]')

    url = 'https://news.naver.com'

    soup = create_soup(url)
    news_list = soup.find('ul', attrs={'class':'hdline_article_list'}).find_all('li', limit=3)

    for idx, news in enumerate(news_list):
        title = news.find('a').get_text().strip()
        link = url + news.find('a')['href']
        print_news(idx, title, link)

def scrape_it_news():
    # 네이버 헤드라인 뉴스 가져오기
    print('[IT 뉴스]')

    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'

    soup = create_soup(url)
    news_list = soup.find('ul', attrs={'class':'type06_headline'}).find_all('li', limit=3)
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find('img')
        if img:
            a_idx = 1   # img 태그가 있으면 1번째 a 태그의 정보를 사용

        a_tag = news.find_all('a')[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag['href']
        print_news(idx, title, link)

def scrape_english():
    print('[오늘의 영어 회화]')

    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'

    soup = create_soup(url)

    sentences = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})

    print('(영어 지문)')
    for sentence in sentences[len(sentences)//2:]:  # 8개의 문장이 있따고 가정했을 떄 index 기준 4~7까지 자른다.
        print(sentence.get_text().strip())

    print('(한글 지문)')
    for sentence in sentences[:len(sentences)//2]:  # 8개의 문장이 있따고 가정했을 떄 index 기준 0~3까지 자른다.
        print(sentence.get_text().strip())

if __name__ == '__main__':
    # scrape_weather()        # 오늘의 날씨 정보 가져오기
    # scrape_headline_news()  # 헤드라인 뉴스 가져오기
    # scrape_it_news()        # 네이버 IT 정보 뉴스 가져오기
    scrape_english()        # 해커스 영어 가져오기



