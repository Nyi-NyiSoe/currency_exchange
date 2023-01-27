from forex_python.converter import CurrencyRates
import PIL.Image
from PIL import ImageTk
from tkinter import *

images = {"usa.png","thai.png","mm.png"}
root = Tk()
root.title("Currency Exchange App")
root.geometry('{}x{}'.format(525,400))

frame = Frame(root,width=100,height=25).grid(row=0,columnspan=3)

e1 = StringVar()
Entry(frame,justify=CENTER,borderwidth=5,font="20",relief=SUNKEN,textvariable=e1).grid(row=0,column=0,padx=7)

Label(frame,font=20,text="<=====>",relief=SUNKEN).grid(row=0,column=1,padx=20,pady=20)

e2 = StringVar()
Entry(frame,justify=CENTER,borderwidth=5,font="20",relief=SUNKEN,textvariable=e2).grid(row=0,column=3,padx=10)

img1 = PIL.Image.open("images/usa.png")
img_var1 = ImageTk.PhotoImage(img1)
Label(frame,relief=SUNKEN,image=img_var1).grid(row=1,column=0)

img2 = PIL.Image.open("images/thai.png")
img_var2 = ImageTk.PhotoImage(img2)
Label(frame,relief=SUNKEN,image=img_var2).grid(row=1,column=3)


images = {""}
root.mainloop()