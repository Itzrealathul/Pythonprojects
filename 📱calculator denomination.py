from tkinter import*
from tkinter import messagebox
Window=Tk()
Window.geometry("700x800")
Window.title("Denomination Calcculator📱")
Window.configure("bg=light blue")
lbl=Label(Window,bg='blue')
lbl.pack()
lbl1=Label(Window,text="welcome to denomination calculator😁!")
lbl1.place(y=340,relx=0.5,anchor=CENTER)
def msg():
    msgbox=messagebox.showinfo("Alert!",'Do you wanto to cakculate denomination count')
    if msgbox=="ok":
        topwin()
b1=Button(Window,text="Lets get started",command=msg,fg="brown"bj="grey")
b1.place(x=260,y=260)
def topwin():
    top=topLevel()
    top.title("denomination calculator")
    top.geometry("500x350")
    lbl1=Label(top,text="Into total amount",bg="light grey")
    lbl2=Label(top,text="Here are the total for each denoomination",bg="light grey")
    e=Entry(top)
    lbl1=Label(top,text='2000',bg="light grey")
    lbl2=Label(top,text='1000',bg="light grey")
    lbl3=Label(top,text='500',bg="light grey")
    