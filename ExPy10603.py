# 파이썬 기초부터 활용까지 (2020.09)
# [6과] list(리스트)

# 리스트의 중첩
a = [1, 2, 3]
b = [a, '한국', '미국']

print(b)            # [[1, 2, 3], '한국', '미국']
print(b[0])         # [1, 2, 3]
print(b[0][1])      # 2