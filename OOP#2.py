import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 



# variable ng colors para sa design ng program note: dito nag bebase lahat ng kulay sa program
light_green = "#9bbc0f"    
dark_green = "#0f380f"  
med_green = "#306230"   


window = tk.Tk()
window.title("Group ng mga may BITAW")
window.geometry("350x300")
window.resizable(False, False)
window.configure(bg=light_green)  


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

# Title ng program with design sa loob ng ()
tk.Label(window, text="GROUP NG MGA MAY BITAW", 
         font=("Courier", 12, "bold"), 
         bg=light_green, fg=dark_green).pack(pady=10)

# text ng enter amount
tk.Label(window, text="Enter Amount (₱):", 
         bg=light_green, fg=dark_green, 
         font=("Courier", 9)).pack()

# Style ng text box na pwedeng mag lagay ng input
tk.Entry(window, textvariable=amount, 
         bg="#e0f8d0", fg=dark_green, 
         font=("Courier", 9)).pack(pady=5)

tk.Label(window, text="Shipping Method:", 
         bg=light_green, fg=dark_green, 
         font=("Courier", 9)).pack()

# settings/design ng radio button 
style = ttk.Style()
style.configure("TRadiobutton",
                background=light_green,
                foreground=dark_green,
                font=("Courier", 8))

ttk.Radiobutton(window, text="Priority $14.95", variable=shipping, value="priority").pack(anchor="w", padx=100)
ttk.Radiobutton(window, text="Express $11.95", variable=shipping, value="express").pack(anchor="w", padx=100)
ttk.Radiobutton(window, text="Standard $5.95", variable=shipping, value="standard").pack(anchor="w", padx=100)

#-----------------------------------------------


tk.Label(window, text="Total (with VAT):", 
         bg=light_green, fg=dark_green, 
         font=("Courier", 9)).pack(pady=10)

# Style ng text box na hindi pwedeng lagyan ng input
tk.Entry(window, textvariable=result, state="readonly", 
         bg="#e0f8d0", fg=dark_green, 
         font=("Courier", 9)).pack()

frame = tk.Frame(window, bg=light_green)  # CHANGED
frame.pack(pady=10)

# compute and clear btn
tk.Button(frame, text="COMPUTE", command=compute,
          bg=med_green, fg="white",
          font=("Courier", 9)).grid(row=0, column=0, padx=5)

tk.Button(frame, text="CLEAR", command=clear,
          bg=med_green, fg="white",
          font=("Courier", 9)).grid(row=0, column=1, padx=5)

window.mainloop()
