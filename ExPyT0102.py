# 네이버 클라우드 플랫폼 가격정보 알아오기 : 테스트 중

# BeautifulSoup : 가볍고 빠르지만 동적Html을 가져오기 힘들다.
# Selenium : 느리고, 메모리를 많이 차지하지만 인터넷에서 데이터를 가져오기 수월하다.

from bs4 import BeautifulSoup
import requests
import re                       # 정규식 라이브러리
import pandas as pd
import openpyxl

def main():

    resp = requests.get('https://www.ncloud.com/charge/region/ko')
    resp.encoding = 'utf-8'  # 혹은 'euc-kr
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')

    lst = soup.find('div', class_='price-detail')
    title = list()

    for item in lst.find_all('h3'):
    # for item in lst.find_all('div', class_='tab-title'):
    # 하위 테이블에 대한 내역을 해야 하는데 하드코딩 하려닌 힘들다. 다른 방법을 찾아야 함
        if item.text == 'Server':
            title.append(item.text + ' VPC')
            title.append(item.text + ' Classic 2세대')
            title.append(item.text + ' Classic 1세대')
        elif item.text == 'SSD Server':
            title.append(item.text + ' VPC')
            title.append(item.text + ' Classic 2세대')
            title.append(item.text + ' Classic 1세대')
        elif item.text == 'GPU Server':
            title.append(item.text + ' VPC')
            title.append(item.text + ' Classic')
        elif item.text == 'Object Storage':
            title.append(item.text + ' 데이터 저장량 요금')
            title.append(item.text + ' API 요청수 요금')
            title.append(item.text + ' 네트워크 전송 요금')
            title.append(item.text + ' VPC 내 사설 통신')
        elif item.text == 'Archive Storage':
            title.append(item.text + ' 데이터 저장량 요금')
            title.append(item.text + ' API 요청수 요금')
            title.append(item.text + ' 네트워크 전송 요금')
        elif item.text == 'Load Balancer':
            title.append('VPC ' + item.text)
            title.append('Classic ' + item.text)
        elif item.text == 'Private Subnet':
            title.append(item.text + ' 요금')
            title.append(item.text + ' Peering 요금')
        elif item.text == 'WORKPLACE':
            title.append(item.text + ' 요금')
            title.append(item.text + ' 법인카드 연동')
            title.append(item.text + ' 용량')
        elif item.text == 'Simple & Easy Notification Service':
            title.append(item.text + ' 요금')
            title.append(item.text + ' 국제 SMS')
        elif item.text == 'Cloud DB for MySQL':
            title.append(item.text + ' VPC')
            title.append(item.text + ' Classic')
            title.append(item.text + ' 데이터 스토리지')
            title.append(item.text + ' 백업 스토리지')
        elif item.text == 'Tmax':
            title.append(item.text + ' 라이선스')
            title.append(item.text + ' 기술 지원')
        elif item.text == 'Cloud Hadoop':
            title.append(item.text + ' 인스턴스 가격')
            title.append(item.text + ' 스토리지 요금')
            title.append(item.text + ' 저장량 요금')
            title.append(item.text + ' 처리')
        elif item.text == 'Cloud DB for Redis':
            title.append(item.text + ' VPC')
            title.append(item.text + ' Classic')
            title.append(item.text + ' 백업 스토리지')
        elif item.text == 'Global Route Manager':
            title.append(item.text + ' 리소스')
            title.append(item.text + ' 쿼리수')
        elif item.text == 'Cloud DB for MSSQL':
            title.append(item.text + ' 서버')
            title.append(item.text + ' 데이터 스토리지')
            title.append(item.text + ' 백업 스토리지')
        elif item.text == 'Secure Zone':
            continue
        elif item.text == 'CLOVA Chatbot':
            title.append(item.text + ' 대화 모델 빌드')
            title.append(item.text + ' 대화 학습')
        else:
            title.append(item.text[0:29])
        # print(item.text)

    # print(title)
    # print(len(title))

    with pd.ExcelWriter('ExPyT0102.xlsx') as writer:
        for i in range(len(title)):
            name = pd.read_html('https://www.ncloud.com/charge/region/ko', header=0)[i]
            name.to_excel(writer, sheet_name=title[i])

if __name__ == '__main__':
    main()
