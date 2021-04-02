# 연습문제
# 송파헬리오 시트 부동산 메물 가격 정보
import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=thdvkgp&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0'
heades = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'

res = requests.get(url=url)
res.raise_for_status()
# res = requests.get(url=url, heades=heades)

soup = BeautifulSoup(res.text, 'lxml')

# with open('apt.html', 'w', encoding='utf8') as f:
#     f.write(soup.prettify())

# apts = soup.find('table', attrs={'class':'tbl'})
#
# for idx, apart in enumerate(apts):
#     a1 = apart.find('td', attrs={'class':'col1'}).get_text()
#     a2 = apart.find('td', attrs={'class':'col2'}).get_text()
#     a3 = apart.find('td', attrs={'class':'col3'}).get_text()
#     a4 = apart.find('td', attrs={'class':'col4'}).get_text()
#     a5 = apart.find('td', attrs={'class':'col5'}).get_text()
#     print('======== 매물', idx+1, '========='  )
#     print(f'거래 : {a1}')
#     print(f'면적 : {a2}')
#     print(f'가격 : {a3}')
#     print(f'동 : {a4}')
#     print(f'층 : {a5}')

apts = soup.find('table', attrs={'class':'tbl'}).find('tbody').find_all('tr')

print(apts)

for idx, apt in enumerate(apts):
    columns = apt.find_all('td')

    print('============== 매뭏 {} =============='.format(idx+1))
    print('거래 :', columns[0].get_text().strip())
    print('면적 :', columns[1].get_text().strip(), '(공급/전용)')
    print('가격 :', columns[2].get_text().strip(), '(만원)')
    print('동 :', columns[3].get_text().strip())
    print('층 :', columns[4].get_text().strip())