import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Payslip")
window.geometry("500x500")
window.resizable(False, False)

# data pinag sama sama na para di magulo
data = {
    "Manager": (25000, 28000, 20),
    "System Administrator": (20000, 23000, 15),
    "System Analyst": (15000, 17000, 12),
    "Programmer": (10000, 12000, 10),
    "Technician": (8000, 9000, 7),
    "Encoder": (6000, 6600, 5),
    "Messenger": (5000, 5500, 4)
}

# variable naka ayos para di magulo
name = tk.StringVar()
position = tk.StringVar()
ot_hours = tk.StringVar()
pay_grade = tk.StringVar()
gross = tk.StringVar()
tax = tk.StringVar()
sss = tk.StringVar()
net = tk.StringVar()

SSS = 200

# Pang compute ng salary
def compute():
    try:
        pos = position.get()
        grade = pay_grade.get()

        ot_val = ot_hours.get()

        if ot_val == "":
            ot = 0
        else:
            ot = float(ot_val)

        if pos not in data or grade == "":
            messagebox.showwarning("Incomplete Data", "Please select a Position and Pay Grade.")
            return

        gradeA, gradeB, tax_rate = data[pos]

        if grade == "A":
            basic = gradeA
        else:
            basic = gradeB

        ot_pay = ot * (0.01 * basic)
        gross_pay = basic + ot_pay
        tax_pay = gross_pay * (tax_rate / 100)

        total_deduction = SSS + tax_pay
        net_pay = gross_pay - total_deduction

        gross.set(str(round(gross_pay, 2)))
        tax.set(str(round(tax_pay, 2)))
        sss.set("200")
        net.set(str(round(net_pay, 2)))

        details = (
            "Name: " + name.get() + "\n" +
            "Position: " + pos + "\n" +
            "OT Hours: " + str(ot) + "\n" +
            "Pay Grade: " + grade + "\n" +
            "-----------------------------------\n" +
            "Gross Salary: ₱" + str(round(gross_pay, 2)) + "\n" +
            "Tax: ₱" + str(round(tax_pay, 2)) + "\n" +
            "SSS: ₱200\n" +
            "Net Salary: ₱" + str(round(net_pay, 2))
        )

        messagebox.showinfo("Payslip Details", details)

    except ValueError:
        messagebox.showerror("Error", "Invalid input for OT Hours. Please enter a valid number.")

# pang clear
def clear():
    name.set("")
    position.set("")
    ot_hours.set("")
    pay_grade.set("")
    gross.set("")
    tax.set("")
    sss.set("")
    net.set("")

# title
tk.Label(window, text="PAYSLIP", font=("Arial", 14, "bold")).pack(pady=10)

# name
tk.Label(window, text="Name").pack()
tk.Entry(window, textvariable=name).pack()

# postion
tk.Label(window, text="Position").pack()
tk.OptionMenu(window, position, *data.keys()).pack()

# ot ni porman
tk.Label(window, text="OT Hours").pack()
tk.Entry(window, textvariable=ot_hours).pack()

# pay grade
tk.Label(window, text="Pay Grade").pack()
tk.Radiobutton(window, text="A", variable=pay_grade, value="A").pack()
tk.Radiobutton(window, text="B", variable=pay_grade, value="B").pack()

# output 
tk.Label(window, text="Gross Salary").pack()
tk.Entry(window, textvariable=gross, state="readonly").pack()

tk.Label(window, text="Tax").pack()
tk.Entry(window, textvariable=tax, state="readonly").pack()

tk.Label(window, text="SSS").pack()
tk.Entry(window, textvariable=sss, state="readonly").pack()

tk.Label(window, text="Net Salary").pack()
tk.Entry(window, textvariable=net, state="readonly").pack()

# button na de pindot
frame = tk.Frame(window)
frame.pack(pady=10)

tk.Button(frame, text="Compute", command=compute).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Clear", command=clear).grid(row=0, column=1, padx=5)

window.mainloop()
