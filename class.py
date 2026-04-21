import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("380x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")

        self.expression = ""
        self.result_shown = False
        self.history = []

        self.display_var = tk.StringVar(value="0")
        self.expr_var    = tk.StringVar(value="")

        self._build_ui()
        self._bind_keys()

    def _build_ui(self):
        BG      = "#1a1a2e"
        DISP_BG = "#16213e"
        NUM_BG  = "#0f3460"
        NUM_HOV = "#1a4a7a"
        OP_BG   = "#e94560"
        OP_HOV  = "#ff6b7a"
        FUNC_BG = "#16213e"
        FUNC_HOV= "#253050"
        FG_MAIN = "#eaeaea"
        FG_DIM  = "#7a8fa6"

        # display
        disp = tk.Frame(self.root, bg=DISP_BG, padx=20, pady=18)
        disp.pack(fill="x")

        tk.Label(disp, textvariable=self.expr_var,
                 bg=DISP_BG, fg=FG_DIM,
                 font=("Courier New", 13),
                 anchor="e", justify="right").pack(fill="x")

        tk.Label(disp, textvariable=self.display_var,
                 bg=DISP_BG, fg=FG_MAIN,
                 font=("Courier New", 38, "bold"),
                 anchor="e", justify="right").pack(fill="x")

        # button grid
        grid = tk.Frame(self.root, bg=BG, padx=12, pady=12)
        grid.pack(fill="both", expand=True)

        def btn(parent, text, row, col, cmd, bg, fg, hov):
            b = tk.Button(parent, text=text, command=cmd,
                          bg=bg, fg=fg,
                          activebackground=hov, activeforeground=fg,
                          font=("Courier New", 16, "bold"),
                          relief="flat", bd=0, cursor="hand2")
            b.grid(row=row, column=col, padx=5, pady=5,
                   sticky="nsew", ipadx=4, ipady=12)
            b.bind("<Enter>", lambda e, b=b, h=hov: b.config(bg=h))
            b.bind("<Leave>", lambda e, b=b, c=bg:  b.config(bg=c))

        N = NUM_BG; NH = NUM_HOV
        O = OP_BG;  OH = OP_HOV
        F = FUNC_BG;FH = FUNC_HOV
        W = FG_MAIN

        layout = [
            ("C",  0,0, self.clear,              F,"#e94560",FH),
            ("⌫",  0,1, self.backspace,           F, W, FH),
            ("%",  0,2, lambda:self.append("%"),  F, W, FH),
            ("÷",  0,3, lambda:self.append("/"),  O, W, OH),
            ("7",  1,0, lambda:self.append("7"),  N, W, NH),
            ("8",  1,1, lambda:self.append("8"),  N, W, NH),
            ("9",  1,2, lambda:self.append("9"),  N, W, NH),
            ("×",  1,3, lambda:self.append("*"),  O, W, OH),
            ("4",  2,0, lambda:self.append("4"),  N, W, NH),
            ("5",  2,1, lambda:self.append("5"),  N, W, NH),
            ("6",  2,2, lambda:self.append("6"),  N, W, NH),
            ("−",  2,3, lambda:self.append("-"),  O, W, OH),
            ("1",  3,0, lambda:self.append("1"),  N, W, NH),
            ("2",  3,1, lambda:self.append("2"),  N, W, NH),
            ("3",  3,2, lambda:self.append("3"),  N, W, NH),
            ("+",  3,3, lambda:self.append("+"),  O, W, OH),
            ("√",  4,0, self.sqrt,                F, W, FH),
            ("0",  4,1, lambda:self.append("0"),  N, W, NH),
            (".",  4,2, self.dot,                 N, W, NH),
            ("=",  4,3, self.solve,               O, W, OH),
        ]
        for item in layout:
            btn(grid, *item)

        for i in range(5): grid.rowconfigure(i, weight=1)
        for j in range(4): grid.columnconfigure(j, weight=1)

        # history bar
        hist = tk.Frame(self.root, bg="#0d0d1a", pady=6, padx=16)
        hist.pack(fill="x", side="bottom")
        self.hist_label = tk.Label(hist, text="",
                                   bg="#0d0d1a", fg=FG_DIM,
                                   font=("Courier New", 11),
                                   anchor="w", justify="left")
        self.hist_label.pack(fill="x")

    def _bind_keys(self):
        for ch in "0123456789+-*/.%":
            self.root.bind(ch, lambda e, v=ch: self.append(v))
        self.root.bind("<Return>",    lambda e: self.solve())
        self.root.bind("<KP_Enter>",  lambda e: self.solve())
        self.root.bind("<BackSpace>", lambda e: self.backspace())
        self.root.bind("<Escape>",    lambda e: self.clear())

    def _update(self, main=None, expr=None):
        if main is not None:
            s = str(main)
            if len(s) > 13:
                try: s = f"{float(s):.6g}"
                except: s = s[:13]
            self.display_var.set(s)
        if expr is not None:
            self.expr_var.set(expr)

    def _readable(self, expr):
        return expr.replace("*","×").replace("/","÷").replace("-","−")

    def _fmt(self, v):
        if isinstance(v, float) and v.is_integer():
            return str(int(v))
        return f"{v:.10g}" if isinstance(v, float) else str(v)

    def append(self, value):
        ops = set("+-*/%")
        if self.result_shown:
            self.expression = self.display_var.get() if value in ops else ""
            self.result_shown = False
        last = self.expression[-1:] if self.expression else ""
        if value in ops and last in ops:
            self.expression = self.expression[:-1]
        if value in ops and not self.expression and value not in "+-":
            return
        self.expression += value
        self._update(main=self.expression[-12:] or "0",
                     expr=self._readable(self.expression))

    def dot(self):
        import re
        parts = re.split(r"[+\-*/]", self.expression)
        if "." not in (parts[-1] if parts else ""):
            self.append(".")

    def backspace(self):
        self.result_shown = False
        self.expression = self.expression[:-1]
        self._update(main=self.expression or "0",
                     expr=self._readable(self.expression))

    def clear(self):
        self.expression = ""
        self.result_shown = False
        self._update(main="0", expr="")

    def sqrt(self):
        try:
            val = float(eval(self.expression or "0"))
            if val < 0:
                self._update(main="Error", expr="√ of negative")
                self.expression = ""
                return
            res = math.sqrt(val)
            self._push_history(f"√({self._fmt(val)})", res)
            self.expression = str(res)
            self.result_shown = True
            self._update(main=self._fmt(res),
                         expr=f"√({self._fmt(val)}) =")
        except Exception:
            self._update(main="Error", expr="")
            self.expression = ""

    def solve(self):
        if not self.expression:
            return
        try:
            expr_disp = self._readable(self.expression)
            raw = self.expression.replace("%", "/100")
            result = eval(raw)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self._push_history(expr_disp, result)
            self.expression = str(result)
            self.result_shown = True
            self._update(main=self._fmt(result),
                         expr=f"{expr_disp} =")
        except ZeroDivisionError:
            self._update(main="÷ 0 Error", expr="")
            self.expression = ""
        except Exception:
            self._update(main="Error", expr="")
            self.expression = ""

    def _push_history(self, expr, result):
        self.history.append(f"{expr} = {self._fmt(result)}")
        self.history = self.history[-3:]
        self.hist_label.config(text=self.history[-1])


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()