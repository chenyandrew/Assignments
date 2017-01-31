from tkinter import *
from tkMessageBox import *

root = Tk()

def Butt_Func():
    tkMessagebox.showinfo("To: shell of the sea", "Hey Chelsea, my boo. You're amazing.")

button = Button(center, text="Click me :)", command=Butt_Func)

button.pack()
root.mainloop()
