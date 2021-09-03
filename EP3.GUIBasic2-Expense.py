from tkinter import *
from tkinter import ttk
import csv
from datetime import datetime

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย โดย Old man')
# 500x300+ to specified scale when run dialog 
GUI.geometry('500x400+500+50')


# B1 = Button(GUI,text='OK')
# B1.pack(ipadx=40) # Add button to main GUI, ipadx - internal padding

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)


icon_t1 = PhotoImage(file='t1_expense.png')
icon_t2 = PhotoImage(file='t2_expenselist.png')

Tab.add(T1, text='Add expense',image=icon_t1, compound='top')
Tab.add(T2, text='Total expense',image=icon_t2, compound='top')

# F1 = LabelFrame(GUI, text='test')

F1 = Frame(GUI)
F1.place(x=150, y=50)

days = {'Mon':'จันทร์', 
        'Tue':'อังคาร', 
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี', 
        'Fri':'ศุกร์', 
        'Sat':'เสาร์', 
        'Sun':'อาทิตย์'}


def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()
    total = int(price) * int(quantity)

    today = datetime.now().strftime('%a')
    dt =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dt = days[today] + '-' + dt
    print('รายการ: {} ราคา: {} จำนวน: {} รวมทั้งหมด: {} เวลา: {}' .format(expense,price,quantity,total,dt))
    
    v_expense.set('')
    v_price.set('')
    v_quantity.set('')    

    with open('savedata.csv','a',encoding='utf-8',newline='')as f:
        fw = csv.writer(f)
        data = [expense,price,quantity,total,dt]
        fw.writerow(data)
    E1.focus()
    
GUI.bind('<Return>', Save)    
FONT1 = (None,20) #None change to 'Angsana New'

#-------text1------------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()

v_expense = StringVar() # StringVar() is special variable for store data in GUI

E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------------

#-------text2------------
L2 = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()

v_price = StringVar() # StringVar() is special variable for store data in GUI

E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------------

#-------text3------------
L3 = ttk.Label(F1,text='จำนวน',font=FONT1).pack()

v_quantity = StringVar() # StringVar() is special variable for store data in GUI

E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------------


icon_save = PhotoImage(file='save.png')

B2 = ttk.Button(F1,text='Save',command=Save,image=icon_save,compound='left')
# B2.place(x=20, y=50)
B2.pack(ipadx=50, ipady=20)



GUI.mainloop()
