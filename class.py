from tkinter import *
root = Tk()
root.mainloop()
class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="black")
        master.resizable(0, 0)
        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=16, font=('arial', 20, 'bold'), textvariable=self.equation, bd=10, insertwidth=4, bg="powder blue", justify='right').place(x=0, y=0)
        
