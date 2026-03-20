import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Payslip")
window.geometry("350x350")
window.resizable(False, False)

# DATA
data = {
    "Manager": (25000, 28000, 20),
    "System Administrator": (20000, 23000, 15),
    "System Analyst": (15000, 17000, 12),
    "Programmer": (10000, 12000, 10),
    "Technician": (8000, 9000, 7),
    "Encoder": (6000, 6600, 5),
    "Messenger": (5000, 5500, 4)
}

# VARIABLES
name = tk.StringVar()
position = tk.StringVar()
ot_hours = tk.StringVar()
pay_grade = tk.StringVar()
gross = tk.StringVar()
tax = tk.StringVar()
sss = tk.StringVar()
net = tk.StringVar()

SSS = 200

# FUNCTIONS
def compute():
    try:
        pos = position.get()
        grade = pay_grade.get()
        ot = float(ot_hours.get())

        if pos not in data or grade == "":
            messagebox.showerror("Error", "Complete input")
            return

        gradeA, gradeB, tax_rate = data[pos]
        basic = gradeA if grade == "A" else gradeB

        ot_pay = ot * (0.01 * basic)
        gross_pay = basic + ot_pay
        tax_pay = gross_pay * (tax_rate / 100)
        total = SSS + tax_pay
        net_pay = gross_pay - total

        gross.set(f"{gross_pay:.0f}")
        tax.set(f"{tax_pay:.0f}")
        sss.set("200")
        net.set(f"{net_pay:.0f}")

    except:
        messagebox.showerror("Error", "Invalid input")

def clear():
    name.set("")
    position.set("")
    ot_hours.set("")
    pay_grade.set("")
    gross.set("")
    tax.set("")
    sss.set("")
    net.set("")

# TITLE
tk.Label(window, text="PAYSLIP", font=("Arial", 14, "bold")).pack(pady=10)

# NAME
tk.Label(window, text="Name").pack()
tk.Entry(window, textvariable=name).pack()

# POSITION
tk.Label(window, text="Position").pack()
tk.OptionMenu(window, position, *data.keys()).pack()

# OT
tk.Label(window, text="OT Hours").pack()
tk.Entry(window, textvariable=ot_hours).pack()

# PAY GRADE
tk.Label(window, text="Pay Grade").pack()
tk.Radiobutton(window, text="A", variable=pay_grade, value="A").pack()
tk.Radiobutton(window, text="B", variable=pay_grade, value="B").pack()

# OUTPUTS
tk.Label(window, text="Gross Salary").pack()
tk.Entry(window, textvariable=gross, state="readonly").pack()

tk.Label(window, text="Tax").pack()
tk.Entry(window, textvariable=tax, state="readonly").pack()

tk.Label(window, text="SSS").pack()
tk.Entry(window, textvariable=sss, state="readonly").pack()

tk.Label(window, text="Net Salary").pack()
tk.Entry(window, textvariable=net, state="readonly").pack()

# BUTTONS
frame = tk.Frame(window)
frame.pack(pady=10)

tk.Button(frame, text="Compute", command=compute).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Clear", command=clear).grid(row=0, column=1, padx=5)

window.mainloop()
