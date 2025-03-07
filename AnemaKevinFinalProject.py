"""
Author:  Kevin Anema
Date written: 03/05/2025
Assignment:   Final Project
Short Desc:  Pretzel Ordering System
"""

import tkinter as tk  
from tkinter import messagebox  

# Function to calculate total price including pretzels, dipping sauces, and drinks
def calculate_total():
    try:
        total_pretzel_price = sum(pretzel_prices[pretzel] * int(var.get() or 0) for pretzel, var in pretzel_entries.items())
        total_dipping_sauces_price = sum(dipping_sauces[sauce] * int(var.get() or 0) for sauce, var in dipping_sauce_entries.items())
        total_drinks_price = sum(drinks[drink] * int(var.get() or 0) for drink, var in drink_entries.items())
    except ValueError:
        total_label.config(text="Invalid input detected. Please enter numbers only.")
        return
    
    total = total_pretzel_price + total_dipping_sauces_price + total_drinks_price
    tax = total * 0.07  
    total_with_tax = total + tax
    total_label.config(text=f"Total: ${total_with_tax:.2f} (Including Tax)")
    return total, tax, total_with_tax

# Function to validate and clean input
def validate_input(var):
    value = var.get()
    if not value.isdigit():  
        var.set("")  # Clear invalid input

# Function to place order
def place_order():
    total, tax, total_with_tax = calculate_total()
    
    if total == 0:
        messagebox.showwarning("No Order", "You must order at least one item!")
        return

    order_summary = "Your Order:\n"
    for pretzel, var in pretzel_entries.items():
        quantity = int(var.get() or 0)
        if quantity > 0:
            order_summary += f"{pretzel} (x{quantity}): ${pretzel_prices[pretzel] * quantity:.2f}\n"
    for sauce, var in dipping_sauce_entries.items():
        quantity = int(var.get() or 0)
        if quantity > 0:
            order_summary += f"{sauce} (x{quantity}): ${dipping_sauces[sauce] * quantity:.2f}\n"
    for drink, var in drink_entries.items():
        quantity = int(var.get() or 0)
        if quantity > 0:
            order_summary += f"{drink} (x{quantity}): ${drinks[drink] * quantity:.2f}\n"
    order_summary += f"\nTotal (Before Tax): ${total:.2f}\nTax: ${tax:.2f}\nTotal (Including Tax): ${total_with_tax:.2f}"
    
    popup = tk.Toplevel(root)
    popup.title("Order Confirmation")
    tk.Label(popup, text=order_summary, font=("Arial", 12)).pack(pady=20)
    tk.Button(popup, text="Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=root.quit).pack(pady=10)
    tk.Button(popup, text="Go Back", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=popup.destroy).pack(pady=10)

# Function to exit the program
def exit_program():
    if messagebox.askyesno("Exit", "Do you want to exit the program?"):
        root.quit()

# GUI Setup
root = tk.Tk()
root.title("Kevin's Pretzel Ordering System")
root.geometry("500x800")
root.config(bg="#f5f5f5")
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=20)

tk.Label(frame, text="Kevin's Pretzel Ordering System", font=("Arial", 14, "bold"), bg="#f5f5f5").grid(row=0, column=0, columnspan=2, pady=10)

# Pretzel selection
tk.Label(frame, text="Enter Quantity for Each Pretzel:", font=("Arial", 10), bg="#f5f5f5").grid(row=1, column=0, sticky="w", pady=5)
pretzel_prices = {"Classic": 2.25, "Cinnamon": 2.75, "Pepperoni": 3.25, "Almond": 2.75}
pretzel_entries = {}
row_counter = 2
for pretzel, price in pretzel_prices.items():
    tk.Label(frame, text=f"{pretzel} (${price}):", bg="#f5f5f5").grid(row=row_counter, column=0, sticky="w", padx=10, pady=5)
    var = tk.StringVar()
    var.trace("w", lambda *args, v=var: validate_input(v) or calculate_total())
    pretzel_entries[pretzel] = var
    tk.Entry(frame, textvariable=var, width=5).grid(row=row_counter, column=1, padx=10, pady=5)
    row_counter += 1

# Dipping sauce selection
tk.Label(frame, text="Enter Quantity for Each Dipping Sauce:", bg="#f5f5f5").grid(row=row_counter, column=0, sticky="w", pady=5)
dipping_sauces = {"Cheese": 0.59, "Cream Cheese": 0.59, "Glaze Dip": 0.59, "Honey Mustard": 0.59}
dipping_sauce_entries = {}
row_counter += 1
for sauce, price in dipping_sauces.items():
    tk.Label(frame, text=f"{sauce} (${price}):", bg="#f5f5f5").grid(row=row_counter, column=0, sticky="w", padx=10, pady=5)
    var = tk.StringVar()
    var.trace("w", lambda *args, v=var: validate_input(v) or calculate_total())
    dipping_sauce_entries[sauce] = var
    tk.Entry(frame, textvariable=var, width=5).grid(row=row_counter, column=1, padx=10, pady=5)
    row_counter += 1

# Drink selection
tk.Label(frame, text="Enter Quantity for Each Drink:", bg="#f5f5f5").grid(row=row_counter, column=0, sticky="w", pady=5)
drinks = {"Water": 1.00, "Soda": 1.50, "Lemonade": 1.75, "Iced Tea": 1.75}
drink_entries = {}
row_counter += 1
for drink, price in drinks.items():
    tk.Label(frame, text=f"{drink} (${price}):", bg="#f5f5f5").grid(row=row_counter, column=0, sticky="w", padx=10, pady=5)
    var = tk.StringVar()
    var.trace("w", lambda *args, v=var: validate_input(v) or calculate_total())
    drink_entries[drink] = var
    tk.Entry(frame, textvariable=var, width=5).grid(row=row_counter, column=1, padx=10, pady=5)
    row_counter += 1

# Total and buttons
total_label = tk.Label(frame, text="Total: $0.00", font=("Arial", 12, "bold"), bg="#f5f5f5")
total_label.grid(row=row_counter, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Place Order", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=place_order).grid(row=row_counter+1, column=0, pady=10)
tk.Button(frame, text="Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=exit_program).grid(row=row_counter+1, column=1, pady=10)

root.mainloop()