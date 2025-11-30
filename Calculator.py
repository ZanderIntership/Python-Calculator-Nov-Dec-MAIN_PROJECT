import tkinter as tk

root = tk.Tk()
root.title("Calculator Application")
root.geometry("400x600")


def get_values():
    """Read the two entries and convert to float."""
    v1 = float(Value1Entry.get())
    v2 = float(Value2Entry.get())
    return v1, v2

def add():
    v1,v2 = get_values()
    output_label.config(text=str(v1 + v2))

def Minus():
    v1, v2 = get_values()
    output_label.config(text=str(v1 - v2))

def multiply():
    v1, v2 = get_values()
    output_label.config(text=str(v1 * v2))

def division():
    v1, v2 = get_values()
    output_label.config(text=str(v1 / v2))

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

addBtn = tk.Button(btnFrame, text="+", command=add)
addBtn.grid(row=2, column=0, sticky="w", padx=5, )

MinusBtn = tk.Button(btnFrame, text="-", command=Minus)
MinusBtn.grid(row=2, column=1, sticky="w", padx=5)

DevisionBtn = tk.Button(btnFrame, text="%", command=division)
DevisionBtn.grid(row=2, column=2, sticky="w", padx=5)

MultiplyBtn = tk.Button(btnFrame, text="*", command=multiply)
MultiplyBtn.grid(row=2, column=3, sticky="w", padx=5)

output_frame = tk.Frame(root)
output_frame.pack(side="bottom", pady=20)

output_label_title = tk.Label(output_frame, text="Output", font=("Arial", 12))
output_label_title.pack()

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
