import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Warning", "Password must be at least 8 characters.\nUsing 12 instead.")
            length = 12
    except ValueError:
        messagebox.showerror("Error", "Length must be a number.")
        return

    include_uppercase = var_uppercase.get()
    include_lowercase = var_lowercase.get()
    include_digits = var_digits.get()
    include_symbols = var_symbols.get()

    character_sets = ''
    if include_uppercase:
        character_sets += string.ascii_uppercase
    if include_lowercase:
        character_sets += string.ascii_lowercase
    if include_digits:
        character_sets += string.digits
    if include_symbols:
        character_sets += string.punctuation

    if not character_sets:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(secrets.choice(character_sets) for _ in range(length))
    output_entry.delete(0, tk.END)
    output_entry.insert(0, password)

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x320")
root.resizable(False, False)

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase", variable=var_uppercase).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase", variable=var_lowercase).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Digits", variable=var_digits).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)

output_entry = tk.Entry(root, width=40)
output_entry.pack(pady=10)

root.mainloop()
  
