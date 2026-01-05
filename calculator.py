import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=("Segoe UI", 24),
            borderwidth=0,
            relief="flat",
            bg="#1e1e1e",
            fg="white",
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=20)

        self.create_buttons()

    def create_buttons(self):
        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack()

        buttons = [
            ("AC", 0, 0), ("%", 0, 1), ("÷", 0, 2), ("×", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("-", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("=", 3, 3),
            ("0", 4, 0), (".", 4, 1)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                frame,
                text=text,
                width=6,
                height=2,
                font=("Segoe UI", 14),
                bg="#2d2d2d",
                fg="white",
                borderwidth=0,
                command=lambda t=text: self.on_click(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_click(self, char):
        if char == "AC":
            self.expression = ""
        elif char == "=":
            try:
                expr = self.expression.replace("×", "*").replace("÷", "/")
                self.expression = str(eval(expr))
            except:
                self.expression = "Error"
        else:
            self.expression += char

        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
