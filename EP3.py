from tkinter import *
from tkinter import ttk

GUI = Tk()
# 500x300+ to specified scale when run dialog 
GUI.geometry('500x300+500+50')

# B1 = Button(GUI,text='OK')
# B1.pack(ipadx=40) # Add button to main GUI, ipadx - internal padding

# F1 = LabelFrame(GUI, text='test')

F1 = Frame(GUI)
F1.place(x=200, y=50)

def Hello():
    print('Hello World')

B2 = ttk.Button(F1,text='Hello',command=Hello)
# B2.place(x=20, y=50)
B2.pack(ipadx=50, ipady=20)



GUI.mainloop()
