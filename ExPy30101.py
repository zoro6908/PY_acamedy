# 쉽고 빠르게 배우는 파이썬 GUI 프로그래밍(2020.12)
# 1 차시 : 파이썬 GUI Programming & widget

import tkinter as tk

win = tk.Tk()

ent1 = tk.Entry(win,
                relief='ridge',
                borderwidth=3,
                highlightcolor='red',
                highlightthickness=3,
                highlightbackground='yellow',
                takefocus=True)

ent1.pack()

ent2 = tk.Entry(win,
                relief='ridge',
                borderwidth=3,
                highlightcolor='red',
                highlightthickness=3,
                highlightbackground='yellow',
                takefocus=True)

ent2.pack()

win.mainloop()