import tkinter as tk

root = tk.Tk()
root.title("Calculator Application")
root.geometry("400x600")

total = 0.0
has_total = False  # indicates whether total has been initialized

def read_entries():
    """Return (v1, v2) as floats or raise ValueError."""
    v1 = float(Value1Entry.get())
    v2 = float(Value2Entry.get())
    return v1, v2

def show_total():
    output_label.config(text=str(total))

def add():
    global total, has_total
    v1, v2 = read_entries()
    if not has_total:
        total = v1 + v2
        has_total = True
    else:
        total = total + v2
    show_total()

def minus():
    global total, has_total
    v1, v2 = read_entries()
    if not has_total:
        total = v1 - v2
        has_total = True
    else:
        total = total - v2
    show_total()

def multiply():
    global total, has_total
    v1, v2 = read_entries()
    if not has_total:
        total = v1 * v2
        has_total = True
    else:
        total = total * v2
    show_total()

def division():
    global total, has_total
    v1, v2 = read_entries()
    if v2 == 0:
        output_label.config(text="Cannot divide by 0")
        return

    if not has_total:
        total = v1 / v2
        has_total = True
    else:
        total = total / v2
    show_total()

def clear():
    global total, has_total
    total = 0.0
    has_total = False
    output_label.config(text="")

# ----- UI -----

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

label1 = tk.Label(input_frame, text="Value 1")
label1.grid(row=0, column=0, sticky="w", padx=5)

Value1Entry = tk.Entry(input_frame)
Value1Entry.grid(row=0, column=1, sticky="w", padx=5)

label2 = tk.Label(input_frame, text="Value 2")
label2.grid(row=1, column=0, sticky="w", padx=5)

Value2Entry = tk.Entry(input_frame)
Value2Entry.grid(row=1, column=1, sticky="w", padx=5)

btnFrame = tk.Frame(root)
btnFrame.pack(pady=10)

tk.Button(btnFrame, text="+", command=add).grid(row=2, column=0, padx=15)
tk.Button(btnFrame, text="-", command=minus).grid(row=2, column=1, padx=15)
tk.Button(btnFrame, text="/", command=division).grid(row=2, column=2, padx=15)
tk.Button(btnFrame, text="*", command=multiply).grid(row=2, column=3, padx=15)
tk.Button(btnFrame, text="C", command=clear).grid(row=2, column=4, padx=15)

output_frame = tk.Frame(root)
output_frame.pack(side="bottom", pady=20)

tk.Label(output_frame, text="Output", font=("Arial", 12)).pack()

output_label = tk.Label(
    output_frame,
    text="",
    font=("Arial", 18),
    width=20,
    height=2,
    relief="solid",
    anchor="center"
)
output_label.pack(pady=5)

root.mainloop()
