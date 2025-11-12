from tkinter import*
window=Tk()
window.geometry("250x300")
f=Frame(master=window,height=200,width=300 , bg="beige")
nums= [[9,8,7],[6,5,4],[3,2,1],["*",0,"#"]]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        f=Frame(master=window,relief=SUNKEN,borderwidth=1)
        f.grid(row=i,col=j)
        l=Label(master=f,text=nums[i][j],bg='cyan')
        l.pack(padx=3,pady=3)
window.mainloop()