import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Group ng mga may BITAW")
window.geometry("500x350")


amount = tk.StringVar()
shipping = tk.StringVar()
result = tk.StringVar()

def compute():
    try:
        amt = float(amount.get())

        ship_cost = 0

        if shipping.get() == "priority":
            ship_cost = 350.10
        elif shipping.get() == "express":
            ship_cost = 250.50
        elif shipping.get() == "standard":
            if amt > 75:
                ship_cost = 0
            else:
                ship_cost = 150.45

        total = (amt + ship_cost) * 1.12  
        result.set(f"₱ {total:.2f}")

    except:
        messagebox.showerror("Error", "Enter valid amount")

def clear():
    amount.set("")
    shipping.set("")
    result.set("")

tk.Label(window, text="Group ng mga may BITAW", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(window, text="Total amount of your order (₱):").pack()
tk.Entry(window, textvariable=amount).pack(pady=5)

frame_shipping = tk.LabelFrame(window, text="Method ng shipping king ina mo!", font=("Arial", 10))
frame_shipping.pack(padx=20, pady=10, fill="x")

tk.Radiobutton(frame_shipping, text="Priority (overnight) ₱350.10", variable=shipping, value="priority").pack(anchor="w", padx=20)
tk.Radiobutton(frame_shipping, text="Express (2 days) ₱250.50", variable=shipping, value="express").pack(anchor="w", padx=20)
tk.Radiobutton(frame_shipping, text="Standard (5-7 days) ₱150.45", variable=shipping, value="standard").pack(anchor="w", padx=20)

tk.Label(window, text="Amount Payable (12% VAT included):").pack(pady=10)
tk.Entry(window, textvariable=result, state="readonly").pack()

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Button(frame, text="Compute", command=compute).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Clear", command=clear).grid(row=0, column=1, padx=5)

window.mainloop()
