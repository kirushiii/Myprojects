import tkinter as tk
from tkinter import messagebox

# Bill Calculation
def calculate_bill(units, customer_type):
    if customer_type == "Domestic":
        return units * 5
    else:
        return units * 8

# Usage Classification
def classify_usage(units):
    if units < 100:
        return "Low"
    elif units < 300:
        return "Medium"
    else:
        return "High"

# Button Click Function
def submit():
    name = entry_name.get()
    units_text = entry_units.get()
    customer_type = customer_var.get()

    # Validation
    if name == "" or units_text == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        units = float(units_text)
    except:
        messagebox.showerror("Error", "Units must be a number")
        return

    bill = calculate_bill(units, customer_type)
    category = classify_usage(units)

    # Output
    result.set(f"Name: {name}\nUnits: {units}\nType: {customer_type}\nUsage: {category}\nBill: ₹{round(bill,2)}")

# Main Window
root = tk.Tk()
root.title("Electricity Bill Calculator")
root.geometry("350x300")

# Name
tk.Label(root, text="Customer Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Units
tk.Label(root, text="Units Consumed").pack()
entry_units = tk.Entry(root)
entry_units.pack()

# Customer Type
tk.Label(root, text="Customer Type").pack()
customer_var = tk.StringVar(value="Domestic")
tk.Radiobutton(root, text="Domestic", variable=customer_var, value="Domestic").pack()
tk.Radiobutton(root, text="Commercial", variable=customer_var, value="Commercial").pack()

# Button
tk.Button(root, text="Calculate", command=submit).pack(pady=10)

# Result
result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").pack()

# Run App
root.mainloop()