# 파이썬 기초부터 활용까지 (2020.09)
# [11과] 컴퓨터 내부 데이터표현 요약

# 파이썬 문자변환 코드변환 함수
# chr(번호)함수 : 코드번호를 해당되는 문자로 변환한다
# ord(문자)함수 : 문자에 해당하는 코드번호를 반환
for i in range(60, 80):
    print(i, '--->', chr(i))

print(ord('A'))                # 65
print(ord('강'))               # 44053
print(chr(44053))              # 강

# 파이썬 진수의 표현
# 2진수 : '0b' : 0b0101
# 8진수 : '0o' : 0o32
# 16진수 : '0x' : 0xff
print(0xcd)                    # 205
print(0xff)                    # 255
print(0x11)                    # 17
print(0b11111111)              # 255
print(0x3c)                    # 60

# 파이썬 진법변환 함수
# 2진수로 : bin()
# 8진수로 : oct()
# 16진수로 : hex()
# format() 함수 활용
print(bin(3))                  # 0b11
# print(bin(3)+10)             # TypeError: can only concatenate str (not "int") to str
print(bin(3)+'korea')          # 0b11korea
print(hex(255))                # 0xff
format(3, 'b')                 # 205
format(200, '#b')              # 205
format(200, 'x')               #
format(200, '#x')              #
print(int('0xcd', 16))         #
print(int('cd', 16))           #
print(int('45', 16))           # 69
print(int('1001', 2))          # 9