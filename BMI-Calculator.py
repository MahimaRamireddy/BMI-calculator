from cgitb import text
from tkinter import *
from tkinter import messagebox
def height():
    height=float(E1.get())
    return height
def weight():
    weight=float(E2.get())
    return weight

def calculate_BMI(a=""):
    print(a)
    try:
        Height=height()
        Weight=weight()
        bmi=Weight/(Height*Height)
    except ZeroDivisionError:
        messagebox.showinfo("Error", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Error", "Please enter valid data!")
    else:
        BMI=Label(top)
        BMI.config(text=bmi)
        BMI.place(x=200,y=242)
         
         

top=Tk()
#top.configure(background="beige")
top.title("BMI Calculator")
top.geometry("400x400")
top.resizable(width=False, height=False)

L1 = Label(top,text="Height(in Meter)")
L1.place(x=0,y=0)
E1 = Entry(top)
E1.place(x=125,y=0)

L2 = Label(top,text="Weight(in Kg)")
L2.place(x=0,y=100)
E2 = Entry(top)
E2.place(x=125,y=100)

bmi=Label(top,text="BMI")
bmi.place(x=0,y=200)

BUTTON = Button(text=" Calculate",command=calculate_BMI)
BUTTON.grid(row=3, column=0, sticky=W)
BUTTON.place(x=100,y=300)

top.mainloop()
