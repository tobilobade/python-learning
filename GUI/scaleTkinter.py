import tkinter as tk

window = tk.Tk()
window.title("Scale window")
window.geometry("500x300")
i=tk.Label(window, bg="white", fg="red", width=20, text="empty")
i.pack()

def print_selector(v):
    i.configText= ("you have selected"+v)

s=tk.scale.window(label="try-me", from_=0, b=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=1, fg="blue", resolution=1,command=print_selector)
s.pack()
window.mainloop()