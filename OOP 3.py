import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for a cleaner theme

window = tk.Tk()
window.title("Payslip")

window.geometry("450x550") 
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

        gross.set(f"₱ {gross_pay:,.2f}")
        tax.set(f"₱ {tax_pay:,.2f}")
        sss.set("₱ 200.00")
        net.set(f"₱ {net_pay:,.2f}")

        details = (
            "Name: " + name.get() + "\n" +
            "Position: " + pos + "\n" +
            "OT Hours: " + str(ot) + "\n" +
            "Pay Grade: " + grade + "\n" +
            "-----------------------------------------------\n" +
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


# ==========================================
# design ng code
# ==========================================

# clearner ng theme para di mukhang luma 
style = ttk.Style()
if 'clam' in style.theme_names():
    style.theme_use('clam')

# title
tk.Label(window, text="PAYSLIP GENERATOR", font=("Arial", 16, "bold"), fg="#333").pack(pady=15)

input_frame = ttk.Frame(window, padding="20 10 20 10")
input_frame.pack(fill="x")

# name
ttk.Label(input_frame, text="Name:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
ttk.Entry(input_frame, textvariable=name, width=30).grid(row=0, column=1, sticky="w", pady=5, padx=10)

# position ng mag trabaho
ttk.Label(input_frame, text="Position:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
ttk.OptionMenu(input_frame, position, "Select Position", *data.keys()).grid(row=1, column=1, sticky="ew", pady=5, padx=10)

# ot ni porman
ttk.Label(input_frame, text="OT Hours:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
ttk.Entry(input_frame, textvariable=ot_hours, width=30).grid(row=2, column=1, sticky="w", pady=5, padx=10)

# pay grade
ttk.Label(input_frame, text="Pay Grade:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
grade_frame = ttk.Frame(input_frame)
grade_frame.grid(row=3, column=1, sticky="w", pady=5, padx=10)
ttk.Radiobutton(grade_frame, text="A", variable=pay_grade, value="A").pack(side="left", padx=(0, 15))
ttk.Radiobutton(grade_frame, text="B", variable=pay_grade, value="B").pack(side="left")

# Visual Line
ttk.Separator(window, orient='horizontal').pack(fill='x', padx=20, pady=10)

output_frame = ttk.Frame(window, padding="20 0 20 10")
output_frame.pack(fill="x")

# output labels and entries
ttk.Label(output_frame, text="Gross Salary:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
ttk.Entry(output_frame, textvariable=gross, state="readonly", width=25).grid(row=0, column=1, pady=5, padx=10)

ttk.Label(output_frame, text="Tax:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
ttk.Entry(output_frame, textvariable=tax, state="readonly", width=25).grid(row=1, column=1, pady=5, padx=10)

ttk.Label(output_frame, text="SSS:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
ttk.Entry(output_frame, textvariable=sss, state="readonly", width=25).grid(row=2, column=1, pady=5, padx=10)

ttk.Label(output_frame, text="Net Salary:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
ttk.Entry(output_frame, textvariable=net, state="readonly", width=25).grid(row=3, column=1, pady=5, padx=10)

# button na de pindot
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

compute_btn = tk.Button(button_frame, text="Compute", command=compute, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=12)
compute_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", command=clear, bg="#f44336", fg="white", font=("Arial", 10, "bold"), width=12)
clear_btn.grid(row=0, column=1, padx=10)

window.mainloop()
