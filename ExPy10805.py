# 파이썬 기초부터 활용까지 (2020.09)
# [8과] 함수(function) 1

# 본체와 함수간 데이터 흐름
# 전역(global) 변수
from tkinter import *

def change_state():
    global sw
    if sw:
        lbl['state'] = 'active'
    else:
        lbl['state'] = 'disabled'
    sw = not sw

def form_set():
    global lbl
    win = Tk()
    lbl = Label(win, text="안녕 파이썬", font="HY헤드라인M 20", state='active',
                activeforeground='red', disabledforeground='blue')
    lbl.pack()
    btn = Button(win, text='눌러주세요', command=change_state())
    btn.pack()
    return win

if __name__ == '__main__':
    sw = False
    mas = form_set()
    mas.mainloop()