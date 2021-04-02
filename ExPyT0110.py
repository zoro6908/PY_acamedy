# 파이썬 웹 스크랭핑 강의 8
# https://nadocoding.tistory.com/10
# 네이버 '코스피 시가총액 순위' 가져 오기
import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

filename = '코스피 시가총액 순위 1_200.csv'

# f = open(filename, 'w', encoding='utf8', newline='')   # newline은 언터키 먹는 것을 제외
f = open(filename, 'w', encoding='utf-8-sig', newline='')   # 엑셀에서 한글 깨지면
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
writer.writerow(title)

for page in range(1, 2):
    res = requests.get(url=url + str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
    for data_row in data_rows:
        colums = data_row.find_all('td')

        # ['']
        # ['']
        # ['']
        if len(colums) <= 1:                       # 의미 없는 tr 데이터는 skip
            continue
        # 불필요한 공백 없앰
        # data = [colum.get_text() for colum in colums]
        # ['36', '한화솔루션', '49,800', '\n\n\t\t\t\t1,700\n\t\t\t\t\n', '\n\n\t\t\t\t-3.30%\n\t\t\t\t\n', '5,000' ]
        # ['37', '삼성화재', '168,000', '\n\n\t\t\t\t6,500\n\t\t\t\t\n', '\n\n\t\t\t\t-3.72%\n\t\t\t\t\n', '500', ' '']
        # ['38', 'LG디스플레이', '21,750', '\n\n\t\t\t\t1,250\n\t\t\t\t\n', '\n\n\t\t\t\t-5.43%\n\t\t\t\t\n', '5,000', ]
        data = [colum.get_text().strip() for colum in colums]
        # print(data)
        writer.writerow(data)
