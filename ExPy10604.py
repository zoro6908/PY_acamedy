# 파이썬 기초부터 활용까지 (2020.09)
# [6과] list(리스트)

# 리스트 메서드
# 삽입 : append(), insert(), extend()
# 삭제 : remove()
# 기타 : count(), sort(), index(), len()

a = [1, 7, 2, 6, 6, 7]
print(a)                # [1, 7, 2, 6, 6, 7]

a.append(0)             # append 메서드(맨뒤에 0 추가)
print(a)                # [1, 7, 2, 6, 6, 7, 0]

a.insert(2, '김')       # insert 메서드(index 2 위치에 '김' 삽입)
print(a)                # [1, 7, '김', 2, 6, 6, 7, 0]

print(a.count(7))       # count 메서드(7의 갯수를 카운트) : 2
print(a.index('김'))    # index 메소드('김'요소의 인텍스 값을 반화) : 2

# a.sort()              # TypeError: '<' not supported between instances of 'str' and 'int'

a.remove('김')          # remove 메서드 : '김' 제거
print(a)                # [1, 7, 2, 6, 6, 7, 0]

a.sort()                # 다시 sort()
print(a)                # [0, 1, 2, 6, 6, 7, 7]

a.extend([40, 50, 60])  # 리스트 추가 : 각각 개별 요소로 저장
print(a)                # [0, 1, 2, 6, 6, 7, 7, 40, 50, 60]

a.append([40, 50, 60])  # 리스트 추가 : 리스트란 객체로 인식하여 추가
print(a)                # [0, 1, 2, 6, 6, 7, 7, 40, 50, 60, [40, 50, 60]]