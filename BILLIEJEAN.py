import tkinter as tk

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length < 6:
        result_label.config(text="Password Strength: Weak", fg="red")
    elif length <= 10:
        result_label.config(text="Password Strength: Medium", fg="orange")
    else:
        result_label.config(text="Password Strength: Strong", fg="green")


window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("350x200")

title_label = tk.Label(window, text="Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

password_label = tk.Label(window, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(window, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(window, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()