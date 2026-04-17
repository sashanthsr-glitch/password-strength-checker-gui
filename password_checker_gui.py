import re
import tkinter as tk

def check_strength():
    password = entry.get()
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*]", password):
        strength += 1

    if strength <= 2:
        result_label.config(text="Weak ❌", fg="red")
    elif strength == 3:
        result_label.config(text="Medium ⚠️", fg="orange")
    else:
        result_label.config(text="Strong ✅", fg="green")

# Window setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# UI Elements
title = tk.Label(root, text="Enter Password", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, show="*", width=25)
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=check_strength)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()