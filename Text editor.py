from tkinter import*
from tkinter.filedialouge import askopenfilename,asksaveasfilename
window=Tk()
window.title("text editor")
window.geometry("600x400")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(0,minsize=800,weight=1)
def openfile():
    filepath=askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    text_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        Text=input_file.read()
        text_edit.insert(END,text)
        input_file.close()
    window.title(f"text editor-{filepath}")
def savefile():
    filepath=asksaveasfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return 
    with open(filepath,"w") as output_file:
        
        
    
        
        
    
        
        
    
    
