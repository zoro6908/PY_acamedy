# 파이썬 기초부터 활용까지 (2020.09)
# [10과] 튜플과 딕션너리

# 응용 실습 : 관심키워드 설문조사 결과를 키워드 응답숫자를 파악할 수 있도록 프로그램을 작성

k = '''하둡,데이터분석,데이터통계,
포렌식, 모의해킹, 침해대응,
블록체인, 클라우드, 데이터분석,
Security, 5G, 인공지능,
DB, Security, R,
블록체인, 시큐어코딩, 취약점진단,
Iot,클라우드,하이브리드앱,
빅데이터,IOT,
빅데이터,데이터베이스,튜닝,
네트워크, 파이썬, 빅데이터,
4차산업, 인공지능, 빅데이터,
sw아키텍처,프로젝트관리,빅데이터,
스마트컨트랙트, 핀테크, 퀀텀컴퓨팅,
Java, 빅데이터, sql,
Swift 개발, GUI기반 에디터설계,
하   둡, 네트워크보안, 안드로이드앱보안,
자바,스크립트,데이터베이스,
파이썬, nosql, 빅데이터,
클라우드, paas, 파이썬,
오픈소스소프트웨어, 네트워크가상화, 데이터모델링,
딥러닝, IOT, 클라우드,
빅데이터,모바일,자바,
Javascript, webGL, Node
빅데이터,데이터분석,R,Casestudy,
데이터모델링,DATABASE,Security,
파이썬, 서버, iot '''

# 프로그램
k = k.replace(" ","").replace('\n', '').split(',')  #공백을 없애고 ','로 분리
print(type(k), k)

count = {}
for kwd in k:
# setdefault 사용 프로그램
    count.setdefault(kwd, 0)
    count[kwd] = count[kwd] + 1
# if 이용 프로그램
#     if kwd in count:
#         count[kwd] += 1
#     else:
#         count[kwd] = 1

print('\n--------------- 카운팅 출력 결과 ---------------')
for k, v in count.items():
    print('{0:40s} {1:5s}'.format(k, str(v)))



