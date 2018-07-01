from tkinter import *
import time
import random

root=Tk()
root.geometry("1600x800")
root.title("CALCULATOR")

global op
text_input=StringVar()
largeFries=StringVar()
largeBurger=StringVar()
coldDrink=StringVar()
meal=StringVar()
whopper=StringVar()
invoiceNumber=StringVar()
service=StringVar()
cgstsgst=StringVar()
subTotal=StringVar()
total=StringVar()
op=""

largeFries.set(0)
largeBurger.set(0)
coldDrink.set(0)
meal.set(0)
whopper.set(0)


f1=Frame(root,height=200,width=1500,bg="grey")
f1.pack(side=TOP)
f2=Frame(root,height=800,width=1500,bg="lightblue")
f2.pack(side=RIGHT)
f3=Frame(root,height=400,width=1000,bg="lightblue")
f3.pack(side=LEFT)

localtime=time.asctime(time.localtime(time.time()))

lb1=Label(f1,font=("ALGERIAN",40),bg="blue",fg="Yellow",bd=10,text="BILL BANWA LO")
lb2=Label(f1,font=("ALGERIAN",20),bg="Orange",fg="Yellow",bd=10,text=localtime)
lb1.grid()
lb2.grid()

def costOfOrder():
    largeFriesPrice=float(largeFries.get())
    largeBurgerPrice=float(largeBurger.get())
    coldDrinkPrice=float(coldDrink.get())
    mealPrice=float(meal.get())
    whopperPrice=float(whopper.get())
    

    

    
    Toc=largeFriesPrice+largeBurgerPrice+coldDrinkPrice+mealPrice+whopperPrice
    subTotal.set(Toc)

    servicePrice=Toc*0.02
    cgstsgstPrice=Toc*0.05

    totall=Toc+servicePrice+cgstsgstPrice
    service.set(servicePrice)
    cgstsgst.set(cgstsgstPrice)
    total.set(totall)
              

    x=random.randint(10034,699812)
    randomRef=str(x)
    invoiceNumber.set("InvoiceNo:"+randomRef)
    


    

def buttonexit():
    root.destroy()
    

def buttonclick(num):
    global op
    op=op+str(num)
    text_input.set(op)

def buttonclr():
    global op
    op=""
    text_input.set(op)

def buttoneql():
    global op
    ans=str(eval (op))
    text_input.set(ans)
    op=""

def buttonreset():
    largeFries.set(0)
    largeBurger.set(0)
    coldDrink.set(0)
    meal.set(0)
    whopper.set(0)
    invoiceNumber.set("")
    service.set("")
    cgstsgst.set("")
    subTotal.set("")
    total.set("")



lb3=Label(f3,font=("arial",15),text="Large Fries",width=20)
lb3.grid(row=0, column=0)
e2=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=largeFries)
e2.grid(row=0, column=1)

lb4=Label(f3,font=("arial",15),text="Large Burger",width=20)
lb4.grid(row=1, column=0)
e3=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=largeBurger)
e3.grid(row=1, column=1)

lb5=Label(f3,font=("arial",15),text="Cold Drink",width=20)
lb5.grid(row=2, column=0)
e2=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=coldDrink)
e2.grid(row=2, column=1)

lb5=Label(f3,font=("arial",15),text="Meal",width=20)
lb5.grid(row=3, column=0)
e3=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=meal)
e3.grid(row=3, column=1)

lb6=Label(f3,font=("arial",15),text="Whopper",width=20)
lb6.grid(row=4, column=0)
e6=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=whopper)
e6.grid(row=4, column=1)

lb7=Label(f3,font=("arial",15),text="Invoice Number",width=20)
lb7.grid(row=0, column=2)
e7=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=invoiceNumber)
e7.grid(row=0, column=3)

lb8=Label(f3,font=("arial",15),text="Service Charge",width=20)
lb8.grid(row=1, column=2)
e8=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=service)
e8.grid(row=1, column=3)

lb9=Label(f3,font=("arial",15),text="CGST + SGST",width=20)
lb9.grid(row=2, column=2)
e9=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=cgstsgst)
e9.grid(row=2, column=3)

lb10=Label(f3,font=("arial",15),text="Sub Total",width=20)
lb10.grid(row=3, column=2)
e10=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=subTotal)
e10.grid(row=3, column=3)

lb11=Label(f3,font=("arial",15),text="Total",width=20)
lb11.grid(row=4, column=2)
e11=Entry(f3,font=("arial",13),bd=10,bg="Sky blue",justify="left",textvariable=total)
e11.grid(row=4, column=3)



e1=Entry(f2,font=("arial",20),bd=20,bg="Sky blue",justify="right",textvariable=text_input)
e1.grid(columnspan=4)


b1=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(1),font=("arial",10),text="1",bg="light green").grid(row=1,column=0)
b2=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(2),font=("arial",10),text="2",bg="light green").grid(row=1,column=1)
b3=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(3),font=("arial",10),text="3",bg="light green").grid(row=1,column=2)
b4=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(4),font=("arial",10),text="4",bg="light green").grid(row=2,column=0)
b5=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(5),font=("arial",10),text="5",bg="light green").grid(row=2,column=1)
b6=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(6),font=("arial",10),text="6",bg="light green").grid(row=2,column=2)
b7=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(7),font=("arial",10),text="7",bg="light green").grid(row=3,column=0)
b8=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(8),font=("arial",10),text="8",bg="light green").grid(row=3,column=1)
b9=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(9),font=("arial",10),text="9",bg="light green").grid(row=3,column=2)
b0=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick(0),font=("arial",10),text="0",bg="light green").grid(row=4,column=0)
bp=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick('+'),font=("arial",10),text="+",bg="light green").grid(row=1,column=3)
bs=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick('-'),font=("arial",10),text="-",bg="light green").grid(row=2,column=3)
bm=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick('*'),font=("arial",10),text="*",bg="light green").grid(row=3,column=3)
bd=Button(f2,padx=25,pady=15,bd=8,fg="black",command=lambda:buttonclick('/'),font=("arial",10),text="/",bg="light green").grid(row=4,column=3)
beql=Button(f2,padx=25,pady=15,bd=8,fg="black",command=buttoneql,font=("arial",10),text="=",bg="light green").grid(row=4,column=1)
bclr=Button(f2,padx=25,pady=15,bd=8,fg="black",command=buttonclr,font=("arial",10),text="clr",bg="light green").grid(row=4,column=2)

btotal=Button(f3,padx=25,pady=10,bd=8,fg="black",font=("arial",10),text="Total",bg="light green",command=costOfOrder).grid(row=5,column=1)
brst=Button(f3,padx=25,pady=10,bd=8,fg="black",font=("arial",10),text="Reset",bg="light green",command=buttonreset).grid(row=5,column=2)
bext=Button(f3,padx=25,pady=10,bd=8,fg="black",font=("arial",10),text="Exit",bg="light green",command=buttonexit).grid(row=5,column=3)


root.mainloop

