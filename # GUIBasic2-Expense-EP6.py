# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime 
# ttk is theme of Tk

GUI = Tk()
GUI.title('โปรเเกรมบันทึกค่าใช้จ่าย by Nutt')
GUI.geometry('600x700+500+50')

#B1 = Button(GUI,text='Hello')
#B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1 = PhotoImage(file='t1_expense.png') #  .subsample(2) = ย่อรูป
icon_t2 = PhotoImage(file='Picture1.png')

Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}', image=icon_t2,compound='top')

F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()

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
    
        if expense == '':
            print('No Data')
            messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
            return
        elif price == '':
            messagebox.showwarning('Error','กรุณากรอกราคา')
            return
        elif quantity =='':
            quantity = 1
 
        total = float(price) * float(quantity)
        try:
            total = float(price) * float(quantity)
            # .get() คือดึงมาจาก v_expense = StringVar()
            print('รายการ: {} ราคา: {}'.format(expense,price))
            print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
            text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
            text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
            v_result.set
            # clear ข้อมูลเก่า
            v_expense.set('')
            v_price.set('')
            v_quantity.set('')
 
            # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
            today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
            print(today)
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dt = days[today] + '-' + dt
            with open('savedata.csv','a',encoding='utf-8',newline='') as f:
                # with คือสั่งเปิดไฟล์เเล้วปิดอัตโนมัติ
                # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมุลเก่า
                # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
                fw = csv.writer(f) #สร้างฟังชั้นสำหรับเขียนข้อมูล
                data = [dt,expense,price,quantity,total]
                fw.writerow(data)

             # ทำให้เคอเซอร์กลับไปตำเเหน่งช่องกรอก E1
            E1.focus()
        except: 
            print('ERROR')
            messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่')
            v_expense.set('')
            v_price.set('')
            v_quantity.set('')
             #messagebox.showerror ('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
             #messagebox.showinfo ('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')

#ทำให้สามารกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsans New'

#-------Image----------

main_icon = PhotoImage(file='t1_expense.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()


#-------text1----------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปลพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#----------------------

#-------text2----------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปลพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#----------------------

#-------text3----------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปลพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#----------------------

icon_b1 = PhotoImage(file='save_b.png')

B2 = ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('--------ผลลัพธ์--------')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green')
# result = Label(F1, textvariable=v_result,font=FONT1,fg='green')
result.pack(pady=20)
GUI.bind('<Tab>',lambda x: E2.focus())

# TAB2

def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data

def update_record():
    getdata = read_csv()
    v_allrecord.set('')
    text = ''
    for d in getdata:
        txt = '{}---{}---{}---{}---{}\n'.format(d[0],d[1],d[2],d[3],d[4])
        text = text + txt

    v_allrecord.set(text)

v_allrecord = StringVar()
v_allrecord.set('-------All Record-------')
Allrecord = ttk.Label(T2,textvariable=v_allrecord,font=(None,15),foreground='green')
Allrecord.pack()


header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2, columns=header, show='headings',height=10)
result.pack()

for hd in header:
    resulttable.heading(hd,text=hd)

headerwidth = [150,170,80,80,80]
for hd,W in zip(header,headerwidth):
    resulttable.column(hd,width=W)

def update_table():
    getdata = read_csv()
    for dt in getdata:
        resulttable.insert('','end',value=dt)


update_table()

update_record()

GUI.mainloop()
