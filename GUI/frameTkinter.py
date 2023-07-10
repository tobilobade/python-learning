from tkinter import*

def say_hi ():
    print("hello-I")

root=Tk()
frame1=Frame(root)
frame2=Frame(root)
root.title=("Tkinter Frame")


label=Label(frame1, text="label", justify=LEFT, bg="red")
label.pack(side=LEFT)


hi_there= Button(frame2,text="say hi", command=say_hi)
hi_there.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=100,pady=100)

root.mainloop()