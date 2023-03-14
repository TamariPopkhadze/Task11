
from tkinter import *
win = Tk()

win.geometry("700x350")
win.title("Counter of symbols")

def update(event):
   label.config(text="You input "+str(len(text.get("1.0", 'end-1c'))) + " symbols")

text = Text(win)
text.pack()

label = Label(win, text="", justify=CENTER)
label.pack()

text.bind('<KeyPress>', update)
text.bind('<KeyRelease>', update)

win.mainloop()
