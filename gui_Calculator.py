import tkinter as tk

# Function to update expression in text entry
def press(num):
    entry.insert(tk.END, num)

# Function to evaluate the expression
def equalpress():
    try:
        total = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, total)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.config(bg="#1e1e1e")

# Entry field
entry = tk.Entry(root, font=("Arial", 20), border=5, relief="ridge", justify='right', bg="#2e2e2e", fg="white")
entry.pack(pady=10, padx=10, fill="x")

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Frame for buttons
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == "=":
            btn = tk.Button(row_frame, text=btn_text, height=2, width=7, bg="#00b894", fg="white",
                            font=("Arial", 16, "bold"), command=equalpress)
        else:
            btn = tk.Button(row_frame, text=btn_text, height=2, width=7, bg="#2d3436", fg="white",
                            font=("Arial", 16, "bold"), command=lambda t=btn_text: press(t))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

# Clear button
clear_btn = tk.Button(root, text="Clear", height=2, width=28, bg="#d63031", fg="white",
                      font=("Arial", 16, "bold"), command=clear)
clear_btn.pack(pady=10)

root.mainloop()
