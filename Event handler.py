from tkinter import*
window=Tk()
window.geometry("600x400")
window.title("Event handler")
def handle_keypress(event):
    print(event.char)
window.bind ("<Key>",handle_keypress)
b=Button(text="click me")
b.pack()
def handle_click(event):
    print("The button was clicked")
Button.bind("<Button-1>",handle_click)
window.mainloop()