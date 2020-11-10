# 파이썬 기초부터 활용까지 (2020.09)
# [10과] 튜플과 딕션너리

# 딕션너리 : 변수 = {키:값}
my_dict = {'한국':60, '일본':40, '중국':50}
print(my_dict['한국'])                             # 60
my_dict['중국'] = 34                               # 요소 값 변경 가능(키를 이용한 접근)
print(my_dict)                                    # {'한국': 60, '일본': 40, '중국': 34}

# 딕션너리 사용 메서드
for k in my_dict:
    print(k, my_dict[k], end=' ')                 # 한국 60 일본 40 중국 34

print('\n')
for k, v in my_dict.items():                      # items() 메서드
    print(k, v, end=' ')                          # 한국 60 일본 40 중국 34
print('\n')
for v in my_dict.values():                        # values() 메서드
    print(v, end=' ')                             # 60 40 34
print('\n')
for k in my_dict.keys():                          # keys() 메서드
    print(k, end=' ')                             # 한국 일본 중국

if not '베트남' in my_dict:
    print('베트남 없음')                    # 베트남 없음
my_dict['베트남'] = 50                     # 요소 추가
print(my_dict)                            # {'한국': 60, '일본': 40, '중국': 34, '베트남': 50}

j = my_dict.pop('일본'); print(j)          # pop() 메서드 : 40
print(my_dict)                            # {'한국': 60, '중국': 34, '베트남': 50}

b = my_dict.copy(); print(b)              # copy() 메서드 : {'한국': 60, '중국': 34, '베트남': 50}

b['대만'] = 90                             # 요소 추가
print(my_dict)                            # {'한국': 60, '중국': 34, '베트남': 50}
print(b)                                  # {'한국': 60, '중국': 34, '베트남': 50, '대만': 90}

my_dict.clear(); print(my_dict)           # clear() 메서드 : {}

my_dict['미국'] = 20
b.update(my_dict);print(b)                # update() 메서드 : {'한국': 60, '중국': 34, '베트남': 50, '대만': 90, '미국': 20}

a = b.get('캐나다', '없음'); print(a)       # get() 메서드 : 없음
a = b.get('베트남', '없음'); print(a)       # get() 메서드 : 50

a = b.setdefault('한국', 99); print(a)     # setdefault() 메서드 : 60
a = b.setdefault('우간다', 66); print(a)    # setdefault() 메서드 : 99