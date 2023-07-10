# from tkinter import *

# top=Tk()
# L1=Label(top, text="label")
# L1.pack(side=LEFT)
# E1=Entry(top, bd=5)
# E1.pack(side=RIGHT)

# top.mainloop()

import tkinter as tk

window=tk.Tk()
window.title("my window")
window.geometry("500x300")


e1=tk.Entry(window,show=None, font=("Arial",14))
e2=tk.Entry(window,show="", font=("Arial",14))
e3=tk.Button(window, text="submit")

e1.pack(side=RIGHT)
e2.pack()
e3.pack()
window.mainloop()