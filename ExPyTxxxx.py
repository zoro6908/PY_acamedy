import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()

    res.encoding = 'euc-kr'

    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def create_brower(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('winddow-size=1920x1080')

    # headless 없애주는 agent를 받아오기 위해서는
    options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    browser.get(url)
    res = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody')
    return browser

def scrape_salim():

    filename = 'ExPyTxxxx.csv'

    f = open(filename, 'w', encoding='utf-8-sig', newline='')  # 엑셀에서 한글 깨지면
    writer = csv.writer(f)

    for i in range(1, 2):
        url = 'http://salim.ne.kr/home/contents/research/research.php?ptype=&page={}&code=bbs3'.format(i)

        soup = create_soup(url)

        # lsts = soup.find('table', attrs={'style':'layout:fixed;'})
        lsts = soup.find_all('td', attrs={'style':'padding-left:10px;word-break:break-all;'})
        # lsts = soup.find_all('td', attrs={'class': 'num'})
        # print(soup.prettify())
        # print(lsts)

        for lst in lsts:
            # print(lst)
            if lst.find('a').get_text().strip() == '최근 성경공부 목록':
                continue
            elif lst.find('a').get_text().strip() == '성경공부 발제 순서':
                continue
            elif lst.find('a').get_text().strip() == '6월 20일부터 새로운 형식의 발제':
                continue
            elif lst.find('a').get_text().strip() == "발제 새 주제는 ‘정의’":
                continue
            else:
                title = lst.find('a').get_text().strip()
                link = 'http://salim.ne.kr' + lst.find('a')['href']

                # data = [title, link]
                # writer.writerow(data)

                soup1 = create_soup(link)

                # print(soup1.prettify())

                # data_rows = soup1.find_all('td', attrs={'style':'padding-left:10px', 'style':'word-break:break-all;'})
                data_rows = soup1.find_all('td', attrs={'style': ['padding-left:10px', 'word-break:break-all;']})
                # data_rows = soup1.find_all('td', attrs={'style': 'word-break:break-all;'})
                print(data_rows)
                for data_row in data_rows:
                    contents = data_row.get_text().
                    print(contents)


if __name__ == '__main__':
    scrape_salim()