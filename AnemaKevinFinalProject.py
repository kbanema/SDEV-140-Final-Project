"""
Author:  Kevin Anema
Date written: 03/04/2025
Assignment:   Final Project
Short Desc:  Pretzel Ordering Program
"""

import tkinter as tk
from tkinter import messagebox

def calculate_total():
    total_pretzel_price = 0
    for pretzel, var in pretzel_entries.items():
        try:
            quantity = int(var.get()) if var.get() else 0
            total_pretzel_price += pretzel_prices[pretzel] * quantity
        except ValueError:
            continue

    total_dipping_sauces_price = 0
    for sauce, var in dipping_sauce_entries.items():
        try:
            quantity = int(var.get()) if var.get() else 0
            total_dipping_sauces_price += dipping_sauces[sauce] * quantity
        except ValueError:
            continue

    total_drinks_price = 0
    for drink, var in drink_entries.items():
        try:
            quantity = int(var.get()) if var.get() else 0
            total_drinks_price += drinks[drink] * quantity
        except ValueError:
            continue

    total = total_pretzel_price + total_dipping_sauces_price + total_drinks_price

    tax = total * 0.07
    total_with_tax = total + tax

    total_label.config(text=f"Total: ${total_with_tax:.2f} (Including Tax)")

    return total, tax, total_with_tax

def place_order():
    order_summary = "Your Order:\n"
    
    total, tax, total_with_tax = calculate_total()
    

    for pretzel, var in pretzel_entries.items():
        quantity = int(var.get()) if var.get() else 0
        if quantity > 0:
            order_summary += f"{pretzel} (x{quantity}): ${pretzel_prices[pretzel] * quantity:.2f}\n"

    for sauce, var in dipping_sauce_entries.items():
        quantity = int(var.get()) if var.get() else 0
        if quantity > 0:
            order_summary += f"{sauce} (x{quantity}): ${dipping_sauces[sauce] * quantity:.2f}\n"

    for drink, var in drink_entries.items():
        quantity = int(var.get()) if var.get() else 0
        if quantity > 0:
            order_summary += f"{drink} (x{quantity}): ${drinks[drink] * quantity:.2f}\n"
    

    order_summary += f"\nTotal (Before Tax): ${total:.2f}\n"
    order_summary += f"Tax: ${tax:.2f}\n"
    order_summary += f"Total (Including Tax): ${total_with_tax:.2f}"

   
    messagebox.showinfo("Order Placed", order_summary)
    root.quit()

root = tk.Tk()
root.title("Kevin's Pretzel Ordering System")


root.geometry("400x700")
root.minsize(400, 700)


root.config(bg="#f5f5f5")
font = ("Arial", 12)


frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=20)


title_label = tk.Label(frame, text="Kevin's Pretzel Ordering System", font=("Arial", 16, "bold"), bg="#f5f5f5")
title_label.grid(row=0, column=0, columnspan=2, pady=10)


tk.Label(frame, text="Enter Quantity for Each Pretzel:", font=font, bg="#f5f5f5").grid(row=1, column=0, sticky="w", pady=5)
pretzel_entries = {}
pretzel_prices = {"Classic": 2.25, "Cinnamon": 2.75, "Pepperoni": 3.25, "Almond": 2.75}
pretzels = list(pretzel_prices.keys())
for i, pretzel in enumerate(pretzels):
    tk.Label(frame, text=f"{pretzel} (${pretzel_prices[pretzel]}):", font=font, bg="#f5f5f5").grid(row=2+i, column=0, sticky="w", padx=10, pady=5)
    pretzel_var = tk.StringVar()
    pretzel_entries[pretzel] = pretzel_var
    pretzel_entry = tk.Entry(frame, textvariable=pretzel_var, font=font, width=5)
    pretzel_entry.grid(row=2+i, column=1, padx=10, pady=5)
    pretzel_var.trace("w", lambda *args: calculate_total())


tk.Label(frame, text="Enter Quantity for Each Dipping Sauce:", font=font, bg="#f5f5f5").grid(row=6, column=0, sticky="w", pady=5)
dipping_sauce_entries = {}
dipping_sauces = {"Cheese": 0.59, "Cream Cheese": 0.59, "Glaze Dip": 0.59}
for i, sauce in enumerate(dipping_sauces):
    tk.Label(frame, text=f"{sauce} (${dipping_sauces[sauce]}):", font=font, bg="#f5f5f5").grid(row=7+i, column=0, sticky="w", padx=10, pady=5)
    sauce_var = tk.StringVar()
    dipping_sauce_entries[sauce] = sauce_var
    sauce_entry = tk.Entry(frame, textvariable=sauce_var, font=font, width=5)
    sauce_entry.grid(row=7+i, column=1, padx=10, pady=5)
    sauce_var.trace("w", lambda *args: calculate_total())


tk.Label(frame, text="Enter Quantity for Each Drink:", font=font, bg="#f5f5f5").grid(row=10, column=0, sticky="w", pady=5)
drink_entries = {}
drinks = {"Coke": 1.75, "Diet Coke": 1.75, "Lemonade": 2.25, "Bottled Water": 1.25}
for i, drink in enumerate(drinks):
    tk.Label(frame, text=f"{drink} (${drinks[drink]}):", font=font, bg="#f5f5f5").grid(row=11+i, column=0, sticky="w", padx=10, pady=5)
    drink_var = tk.StringVar()
    drink_entries[drink] = drink_var
    drink_entry = tk.Entry(frame, textvariable=drink_var, font=font, width=5)
    drink_entry.grid(row=11+i, column=1, padx=10, pady=5)
    drink_var.trace("w", lambda *args: calculate_total())


total_label = tk.Label(frame, text="Total: $0.00", font=("Arial", 14), bg="#f5f5f5", fg="green")
total_label.grid(row=15, column=0, columnspan=2, pady=20)


place_order_button = tk.Button(frame, text="Place Order", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=place_order, width=20)
place_order_button.grid(row=16, column=0, columnspan=2, pady=10)

root.mainloop()
