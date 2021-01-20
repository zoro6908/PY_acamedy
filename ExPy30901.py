# 쉽고 빠르게 배우는 파이썬 GUI 프로그래밍(2020.12)
# 9 차시 : 키보드 & 마우스 이벤트
# 키보드 이벤트 1 : 키보드를 누르면 키보드의 심볼, 키보드넘버, 키코드를 레이블에 출력

from tkinter import *
from tkinter import ttk

def label_change(e):
    lbl['text'] = e.keysym + ' ' + str(e.keysym_num) + ' ' + str(e.keycode)

win = Tk()
lbl = Label(win, text='키보드를 누르세요', font='굴림20', width='20')
win.bind('<KeyPress>', label_change)
lbl.pack()
win.mainloop()

