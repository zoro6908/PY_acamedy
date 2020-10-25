import matplotlib.pyplot as plt

fig = plt.figure()  # 비어 있는 종이 그리기
ax = fig.add_subplot(111)  # 형번호, 열번호, 그림번호 (종이를 가상으로 나눈 등분)
data = [0, 1]
ax.plot(data)
plt.show()
