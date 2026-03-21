from dataclasses import field
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("User Information System")
window.geometry("350x250")
window.resizable(False, False)

def deets():
    messagebox.showinfo("User Information", "Name: " + name.get() + "\nAddress: " + address.get() + "\nContact Number: " + contact.get() + "\nEmail: " + email.get())

def clr():
    name.delete(0, tk.END)
    address.delete(0, tk.END)
    contact.delete(0, tk.END)
    email.delete(0, tk.END)

main_frame = tk.Frame(window, padx=20, pady=20)
main_frame.pack(expand=True, fill='both')

#Name
name_label=tk.Label(main_frame, text="Name:", font=('Arial', 10))
name_label.grid(row=1, column=0, pady=10)

name=tk.Entry(main_frame, width=25, font=('Arial', 10))
name.grid(row=1, column=2, pady=10)

#address
address_label=tk.Label(main_frame, text="Address:", font=('Arial', 10))
address_label.grid(row=2, column=0, pady=10)

address=tk.Entry(main_frame, width=25, font=('Arial', 10))
address.grid(row=2, column=2, pady=10)

#contact number
contact_label=tk.Label(main_frame, text="Contact Number:", font=('Arial', 10))
contact_label.grid(row=3, column=0, pady=10)

contact=tk.Entry(main_frame, width=25, font=('Arial', 10))
contact.grid(row=3, column=2, pady=10)

#email
email_label=tk.Label(main_frame, text="Email:", font=('Arial', 10))
email_label.grid(row=4, column=0, pady=10)

email=tk.Entry(main_frame, width=25, font=('Arial', 10))
email.grid(row=4, column=2, pady=10)

#buttons
submit_button=tk.Button(main_frame, text="Submit", font=('Arial', 10), width=10, command=deets)
submit_button.grid(row=5, column=0, padx=20, pady=10)

clear_button=tk.Button(main_frame, text="Clear", font=('Arial', 10), width=10, command=clr)
clear_button.grid(row=5, column=2, pady=10)


window.mainloop()