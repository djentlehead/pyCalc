import tkinter as tk
from math import *

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

def clear_entry():
    entry.delete(0, tk.END)

def clear_all():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("(", 5, 0), (")", 5, 1), ("^", 5, 2), ("sqrt(", 5, 3),
    ("sin(", 6, 0), ("cos(", 6, 1), ("tan(", 6, 2), ("log(", 6, 3),
]

for button in buttons:
    text, row, col = button
    btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda text=text: button_click(text))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", padx=20, pady=20, command=clear_entry)
clear_button.grid(row=7, column=0, padx=5, pady=5)

all_clear_button = tk.Button(root, text="AC", padx=20, pady=20, command=clear_all)
all_clear_button.grid(row=7, column=1, padx=5, pady=5)

equal_button = tk.Button(root, text="=", padx=20, pady=20, command=evaluate_expression)
equal_button.grid(row=7, column=2, padx=5, pady=5)

root.mainloop()
