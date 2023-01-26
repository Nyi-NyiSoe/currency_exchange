from forex_python.converter import CurrencyRates

from tkinter import *

root = Tk()
root.title("Currency Exchange App")
root.geometry('{}x{}'.format(525,400))

frame = Frame(root,width=100,height=25).grid(row=0,columnspan=3)

e1 = StringVar()
Entry(frame,justify=CENTER,borderwidth=5,font="20",relief=SUNKEN,textvariable=e1).grid(row=0,column=0,padx=7)

Label(frame,font=20,text="<=====>",relief=SUNKEN).grid(row=0,column=1,padx=20,pady=20)

e2 = StringVar()
Entry(frame,justify=CENTER,borderwidth=5,font="20",relief=SUNKEN,textvariable=e2).grid(row=0,column=3,padx=10)

root.mainloop()