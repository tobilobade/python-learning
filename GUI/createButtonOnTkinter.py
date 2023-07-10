from tkinter import * # import tkinter

class Window(Frame):
    def __init__ (self, master=None):
        Frame.__init__ (self, master)
        self.master= master #widget can take all window
        self.pack (fill=BOTH , expand=1) #fill both means same width and same height
        exitButton= Button(self, text="new button", command =self.clickExitButton, fg="red", bg="yellow")#create button and link  to click exitButton
        exitButton.place(x=0,y=0)# place button at 0,0 cordinates || if you use pack instead of place it will auto align

    def clickExitButton (self):
        exit()





root= Tk() #object created

app=Window(root)

root.wm_title("My Tkinter button") #to give the window a title
root.geometry("320x200")
root.mainloop() #to open the window 

#cordinates x and y axis has origin has top left corner
