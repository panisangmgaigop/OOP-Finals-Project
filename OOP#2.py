import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 


window = tk.Tk()
window.title("Group ng mga may BITAW")
window.geometry("350x300")
window.resizable(False, False)



amount = tk.StringVar()
shipping = tk.StringVar()
result = tk.StringVar()
vat = tk.StringVar()

def compute():
    try:
        amt = float(amount.get())

        ship_cost = 0

        if shipping.get() == "priority":
            ship_cost = 14.95
            vat = 1.12
        elif shipping.get() == "express":
            ship_cost = 11.95
            vat = 1.12
        elif shipping.get() == "standard":
            if amt > 75:
                ship_cost = 0
                vat = 1.12
            else:
                ship_cost = 5.95
                vat = 1.12

        total = (amt + ship_cost) * vat  
        result.set("$" + str(round(total, 2)))
        
        if shipping.get() == "":
            messagebox.showwarning("Incomplete Data", "Choose shipping method")
            return

    except:
        messagebox.showerror("Error", "Enter valid amount")

def clear():
    amount.set("")
    shipping.set("")
    result.set("")

tk.Label(window, text="Group ng mga may BITAW", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(window, text="Total amount of your order (₱):").pack()
tk.Entry(window, textvariable=amount).pack(pady=5)

tk.Label(window, text="Choose shipping method:").pack()

ttk.Radiobutton(window, text="Priority (overnight) $14.95", variable=shipping, value="priority").pack(anchor="w")
ttk.Radiobutton(window, text="Express (2 days) $11.95", variable=shipping, value="express").pack(anchor="w")
ttk.Radiobutton(window, text="Standard (5-7 days) $5.95", variable=shipping, value="standard").pack(anchor="w")

tk.Label(window, text="Amount Payable (12% VAT included):").pack(pady=10)
tk.Entry(window, textvariable=result, state="readonly").pack()

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Button(frame, text="Compute", command=compute).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Clear", command=clear).grid(row=0, column=1, padx=5)

window.mainloop()
