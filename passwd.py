import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])
    if length < 8 or score < 2:
        return "Poor"
    elif length < 12 or score < 3:
        return "Medium"
    else:
        return "Strong"

def on_generate():
    length = password_length.get()
    try:
        length = int(length)
        if length < 4:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Length", "Please enter a valid number (>=4) for length.")
        return
    pwd = generate_password(length)
    password_var.set(pwd)
    strength_var.set(check_strength(pwd))

def on_check():
    pwd = password_entry.get()
    strength_var.set(check_strength(pwd))

# Tkinter UI
root = tk.Tk()
root.title("Password Generator & Strength Checker")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
password_length = tk.StringVar(value="12")
tk.Entry(root, textvariable=password_length, width=5).grid(row=0, column=1, padx=5, pady=5)

tk.Button(root, text="Generate Password", command=on_generate).grid(row=0, column=2, padx=5, pady=5)

password_var = tk.StringVar()
tk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, textvariable=password_var, width=30)
password_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

tk.Button(root, text="Check Strength", command=on_check).grid(row=2, column=0, padx=5, pady=5)

strength_var = tk.StringVar()
tk.Label(root, text="Strength:").grid(row=2, column=1, padx=5, pady=5)
tk.Label(root, textvariable=strength_var, width=10).grid(row=2, column=2, padx=5, pady=5)

root.mainloop()