import tkinter as tk
from tkinter import messagebox
from passw_gen import generate_password

def on_generate():
    try:
        length = int(entry_length.get())
    except ValueError:
        messagebox.showerror("Error", "Enter the correct number")
        return

    pwd = generate_password(length, var_upper.get(), var_digits.get(), var_symbols.get())
    label_result.config(text=pwd)

def copy_to_clipboard():
    password = label_result.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Info", "Password copied to clipboard")

#Konfiguracja głównego okna
root = tk.Tk()
root.title("Password Generator")

#Pole do wprowadzania długości hasła
tk.Label(root, text="Number of characters in the password:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

#Checkboxy dla dodatkowych opcji
var_upper = tk.IntVar(value=1)
var_digits = tk.IntVar(value=1)
var_symbols = tk.IntVar(value=1)

tk.Checkbutton(root, text="Upper letters", variable=var_upper).pack()
tk.Checkbutton(root, text="Digits", variable=var_digits).pack()
tk.Checkbutton(root, text="Symbols", variable=var_symbols).pack()

#Przycisk generujący hasło
btn_generate = tk.Button(root, text="Generate password", command=on_generate)
btn_generate.pack(pady=5)

#Etykieta wyświetlająca wynik
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

#Przycisk kopiowania wygenerowanego hasła
btn_copy = tk.Button(root, text="Copy password", command=copy_to_clipboard)
btn_copy.pack(pady=5)

root.mainloop()
