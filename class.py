from tkinter import *
root = Tk()
root.mainloop()
calculator=Calculator(root)
class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="black")
        master.resizable(0, 0)
        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=16, font=('arial', 20, 'bold'), textvariable=self.equation, bd=10, insertwidth=4, bg="powder blue", justify='right').place(x=0, y=0)

        Button(width=7, height=3, text="1", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(1)).place(x=0, y=100)
        Button(width=7, height=3, text="2", font=('arial',  20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(2)).place(x=90, y=100)
        Button(width=7, height=3, text="3", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(3)).place(x=180, y=100)
        Button(width=7, height=3, text="4", font=('arial',  20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=7, height=3, text="5", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=7, height=3, text="6", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=7, height=3, text="7", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(7)).place(x=0, y=300)
        Button(width=7, height=3, text="8", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(8)).place(x=90, y=300)
        Button(width=7, height=3, text="9", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(9)).place(x=180, y=300)
        Button(width=7, height=3, text="0", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show(0)).place(x=90, y=400)
        Button(width=7, height=3, text="+", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show("+")).place(x=270, y=100)
        Button(width=7, height=3, text="-", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show("-")).place(x=270, y=200)
        Button(width=7, height=3, text="*", font=('arial', 20   , 'bold'), bd=0, bg="powder blue", command=lambda: self.show("*")).place(x=270, y=300)
        Button(width=7, height=3, text="/", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=lambda: self.show("/")).place(x=270, y=400)
        Button(width=7, height=3, text="C", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=self.clear).place(x=0, y=400)
        Button(width=7, height=3, text="=", font=('arial', 20, 'bold'), bd=0, bg="powder blue", command=self.solve).place(x=180, y=400)
        
        def show(self, value):
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

        def clear(self):
            self.entry_value = ""
            self.equation.set(self.entry_value)

        def solve(self):
            result = eval(self.entry_value)
            self.equation.set(result)
