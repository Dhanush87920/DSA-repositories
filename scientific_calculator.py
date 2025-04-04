import tkinter as tk
from math import *

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify='right', bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_texts = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
    ("sin", "cos", "tan", "sqrt"),
    ("log", "ln", "^", "%")
]

for row in button_texts:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for text in row:
        button = tk.Button(frame, text=text, font="Arial 18", relief=tk.GROOVE, height=2, width=5)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        button.bind("<Button-1>", on_click)

root.mainloop()
